from typing import Dict

import torch
import torchvision.models
from torch import nn

from models.classification.base_model import BaseClassificationModel


class EfficientNet(BaseClassificationModel):
    def __init__(self, num_classes: int):
        super().__init__()
        self.model = torchvision.models.efficientnet_b0()
        self.model.classifier[1] = nn.Linear(1280, num_classes)


class EfficientNetFeatureMapExtractor(BaseClassificationModel):
    def __init__(self, model: EfficientNet, num_leave_layers: int = 4):
        super().__init__()
        self.model = nn.Sequential(*list(model.get_model().features)[:-num_leave_layers])

    def forward(self, batch: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        x = batch['frames']
        x = self.model(x)
        return {'feature_maps': x}
