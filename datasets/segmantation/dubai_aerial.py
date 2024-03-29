import os
from typing import Dict, Tuple, Optional, List

import cv2
import torch
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor

from augmentations.augs import RandomCrop, CenterCrop, BaseAug
from datasets import FRAME_KEY, GROUND_TRUTH_KEY

DUBAI_AERIAL_DATASET = 'DUBAI_AERIAL_DATASET'

COLOR_MAP = {
    0: (152, 16, 60),  # building
    1: (246, 41, 132),  # land
    2: (228, 193, 110),  # road
    3: (58, 221, 254),  # vegetation
    4: (41, 169, 226),  # water
    5: (155, 155, 155)  # unlabeled
}

COLOR_MAP_TENSOR = torch.tensor(list(COLOR_MAP.values()), dtype=torch.uint8)


class DubaiAerial(Dataset):
    color_map = COLOR_MAP_TENSOR

    def __init__(self, resolution: Tuple[int, int]):
        super().__init__()
        self.resolution = resolution
        self.crop_train = RandomCrop(self.resolution, target_keys=[FRAME_KEY, GROUND_TRUTH_KEY])
        self.crop_val = CenterCrop(self.resolution, target_keys=[FRAME_KEY, GROUND_TRUTH_KEY])
        self.crop: Optional[BaseAug] = None
        self.transform = ToTensor()
        if DUBAI_AERIAL_DATASET not in os.environ:
            raise RuntimeError('Dataset root not in environment.')
        self.root = os.environ[DUBAI_AERIAL_DATASET]
        tile_list = [tile for tile in sorted(os.listdir(self.root)) if os.path.isdir(os.path.join(self.root, tile))]
        self._image_path_list = []
        self._ground_true_path_list = []
        for tile in tile_list:
            tile_path = os.path.join(self.root, tile)
            self._image_path_list += [os.path.join(tile_path, 'images', img)
                                      for img in sorted(os.listdir(os.path.join(tile_path, 'images')))]
            self._ground_true_path_list += [os.path.join(tile_path, 'masks', img)
                                            for img in sorted(os.listdir(os.path.join(tile_path, 'masks')))]
        for (img_path, gt_path) in zip(self._image_path_list, self._ground_true_path_list):
            if os.path.basename(img_path).split('.')[0] != os.path.basename(gt_path).split('.')[0]:
                raise RuntimeError('Dataset is broken! '
                                   'Check out _image_path_list and _ground_true_path_list correspondence.')

    def setup_mode(self, mode: str, indexes: List[int]):
        """
        Method to setup crop depended on mode before usage.

        :param indexes: indexes to select images and masks to the split.
        :param mode: 'train' or 'val'.
        :return: None
        """
        if mode == 'train':
            self.crop = self.crop_train
        elif mode == 'val':
            self.crop = self.crop_val
        else:
            raise RuntimeError('Mode must be train or val.')
        self._image_path_list = [self._image_path_list[i] for i in indexes]
        self._ground_true_path_list = [self._ground_true_path_list[i] for i in indexes]

    def __len__(self) -> int:
        return len(self._image_path_list)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        img = cv2.imread(self._image_path_list[idx])
        img = self.transform(img)
        gt_color = cv2.imread(self._ground_true_path_list[idx])
        gt_color = (self.transform(gt_color) * 255.).to(torch.uint8)  # (3, h, w)
        gt_color = gt_color.permute(1, 2, 0).unsqueeze(2)  # (h, w, 1, 3)
        res = gt_color - self.color_map  # (h, w, NUM_COLORS, 3)
        gt = torch.argmin(res, dim=2)  # (h, w, 3)
        return self.crop({FRAME_KEY: img, GROUND_TRUTH_KEY: gt.select(2, 0)})
