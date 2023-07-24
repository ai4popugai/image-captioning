import os
from typing import Tuple, List

from torch import nn
from torch.utils.data import Dataset, random_split

from datasets.classification.gpr import GPRDataset, NUM_CLASSES
from experiments.EfficientNet_b0.efficient_net_b0 import EfficientNet
from metricks.classification.accuracy import Accuracy
from metricks.base_metric import BaseMetric
from train.run import Run


class RunBase(Run):
    def __init__(self, filename: str):
        super().__init__(filename)

        self._num_classes = NUM_CLASSES
        self.resolution = (64, 64)

        self.batch_size = 64
        self.num_workers = 8

        self.validation_split = 0.2

        self.optimizer = None
        self.loss = nn.CrossEntropyLoss()

        self.train_metrics: List[BaseMetric] = [Accuracy(self._num_classes)]
        self.val_metrics: List[BaseMetric] = [Accuracy(self._num_classes)]

        self.start_snapshot_name = None

        self.lr_policy = None

    def setup_model(self) -> nn.Module:
        return EfficientNet(num_classes=self._num_classes)

    def setup_datasets(self) -> Tuple[Dataset, Dataset]:
        dataset = GPRDataset(resolution=self.resolution)

        # Split the dataset into training and validation sets (e.g., 80% train, 20% validation)
        dataset_size = dataset.__len__()
        validation_size = int(self.validation_split * dataset_size)
        train_size = dataset_size - validation_size

        train_dataset, validation_dataset = random_split(dataset, [train_size, validation_size])
        return train_dataset, validation_dataset
