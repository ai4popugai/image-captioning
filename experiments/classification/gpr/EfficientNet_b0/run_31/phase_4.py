"""From iteration 10600"""


import os
from typing import Tuple

from torch.utils.data import Dataset

from augmentations.augs import RandomFlip, RotateWithProb, \
    RandomColorJitterWithProb
from datasets.classification.gpr import GPRDataset
from experiments.classification.gpr.EfficientNet_b0.run_base import RunBase
from optim_utils.iter_policy.cosine_policy import CosineAnnealingIterationPolicy


class Phase(RunBase):
    def __init__(self):
        super().__init__(os.path.abspath(__file__))

        self.optimizer_kwargs = {'weight_decay': 2e-4}
        self.lr_policy = CosineAnnealingIterationPolicy(1.5e-4, 6000, 0, 1500)

        self.train_augs = [RandomColorJitterWithProb(probability=0.5, hue_range=(-0.5, 0.5)),
                           RandomColorJitterWithProb(probability=0.5, brightness_range=(0.7, 1)),
                           RandomFlip(), RotateWithProb(probability=0.5)]
        self.val_augs = None

    def setup_datasets(self) -> Tuple[Dataset, Dataset]:
        """
        Provide new train - test 80/20 splits.
        :return: train and val datasets
        """
        dataset = GPRDataset(resolution=self.resolution)

        train_dataset, val_dataset = GPRDataset(resolution=self.resolution), GPRDataset(resolution=self.resolution)
        train_dataset.frames_list = []
        val_dataset.frames_list = []

        for i in range(0, len(dataset), 10):
            files_slice = dataset.frames_list[i: i + 10]
            train_dataset.frames_list += files_slice[:8]
            val_dataset.frames_list += files_slice[8:]
        del dataset
        return train_dataset, val_dataset


if __name__ == '__main__':
    Phase().train(start_snapshot=None)
