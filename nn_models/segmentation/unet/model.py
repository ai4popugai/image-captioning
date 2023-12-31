from typing import Dict, Optional

import torch
from torch import nn
from segmentation_models_pytorch import Unet as Unet_seg_models

from datasets import FRAME_KEY, LOGIT_KEY


class Unet(nn.Module):
    def __init__(self, num_classes: int, encoder_name: str = "resnet34", encoder_weights: Optional[str] = None,
                 decoder_use_batchnorm: bool = True):
        super().__init__()
        self.model = Unet_seg_models(classes=num_classes, encoder_weights=encoder_weights,
                                     decoder_use_batchnorm=decoder_use_batchnorm,
                                     encoder_name=encoder_name,
                                     )

    def forward(self, batch: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        return {LOGIT_KEY: self.model(batch[FRAME_KEY])}
