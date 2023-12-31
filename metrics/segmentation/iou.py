from typing import Dict, Optional

import torch
from torchmetrics import JaccardIndex

from datasets import LOGIT_KEY, GROUND_TRUTH_KEY
from metrics.base_metric import BaseMetric


class IoU(BaseMetric):
    def __init__(self, num_classes, ignore_index: Optional[int] = None):
        super().__init__(name='IoU')
        self.num_classes = num_classes
        self.iou_metric = JaccardIndex(task='multiclass', num_classes=num_classes, ignore_index=ignore_index)
        self.unit = '%'
        self.num_samples = 0
        self.total_iou = 0.
        
    def update(self, result: Dict[str, torch.Tensor], batch: Dict[str, torch.Tensor]) -> None:
        self.total_iou += self.iou_metric(torch.argmax(result[LOGIT_KEY].clone().detach(), dim=1).cpu(),
                                          batch[GROUND_TRUTH_KEY].clone().detach().cpu())
        self.num_samples += 1

    def compute(self):
        return self.total_iou / self.num_samples * 100

    def reset(self):
        self.total_iou = 0.0
        self.num_samples = 0

    def to(self, device: torch.device) -> None:
        self.iou_metric.to(device)
