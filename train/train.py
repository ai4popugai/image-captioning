import os
from typing import List, Tuple, Dict, Any

import torch
from torch import nn
from torch.optim.lr_scheduler import LRScheduler
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter

from metricks.base_metric import BaseMetric


class Trainer:
    def __init__(self,
                 train_dataset: Dataset,
                 val_dataset: Dataset,
                 batch_size: int,
                 num_workers: int,
                 snapshot_dir: str,
                 logs_dir: str,
                 optimizer: torch.optim.Optimizer,
                 loss: nn.Module,
                 metrics: List[BaseMetric],
                 train_iters: int, val_iters: int,
                 show_iters: int,):
        """
        :param train_dataset: dataset for train loop.
        :param val_dataset: dataset for validation loop.
        :param batch_size: batch size for single GPU.
        :param num_workers: number of CPU workers used by DataLoader.
        :param snapshot_dir: directory for snapshots.
        :param logs_dir: directory where to place train logs.
        :param optimizer: initialized optimizer instance.
        :param loss: loss function for optimizations.
        :param metrics: list of metrics to be calculated during training.
        :param train_iters: number of training iterations before validation loop is executed.
        :param val_iters: number of iterations in the validation loop.
        :param show_iters: number of training iterations to accumulate loss for logging to tensorboard.
        """
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.snapshot_dir = snapshot_dir
        self.logs_dir = logs_dir
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics
        self.train_iters = train_iters
        self.val_iters = val_iters
        self.show_iters = show_iters

        if os.path.exists(self.logs_dir) is False:
            os.makedirs(self.logs_dir)
        writer = SummaryWriter(self.logs_dir)
        self.writer = writer

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def train(self, model: nn.Module, start_snapshot_path: str or None, reset_optimizer: bool,
              max_iteration: int,
              lr_policy: LRScheduler or None = None,
              strict_weight_loading: bool = True,
              cudnn_benchmark: bool = True,):

        torch.backends.cudnn.benchmark = cudnn_benchmark
        torch.backends.cudnn.deterministic = False
        torch.backends.cuda.matmul.allow_tf32 = self.allow_tf32  # False to improve numerical accuracy.
        torch.backends.cudnn.allow_tf32 = self.allow_tf32  # False to improve numerical accuracy.

        if start_snapshot_path is not None:
            global_step = self._load_snapshot(model, start_snapshot_path, strict_weight_loading)
        else:
            global_step = 0

        if reset_optimizer:
            self.optimizer.zero_grad()

        train_loader = DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
            pin_memory=True,
            drop_last=True,
        )
        val_loader = DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            pin_memory=True,
            drop_last=False,
        )
        self._train_loop(model, train_loader, val_loader, global_step, max_iteration, lr_policy)

    def _load_snapshot(self, model, start_snapshot_path, strict_weight_loading) -> int:
        checkpoint = torch.load(start_snapshot_path, map_location=self.device)
        model.load_state_dict(checkpoint['model_state_dict'], strict=strict_weight_loading)
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print(f'Loaded snapshot from {start_snapshot_path}')
        return checkpoint['global_step']

    def _save_snapshot(self, model, snapshot_path, global_step):
        torch.save({
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'global_step': global_step,

        }, snapshot_path)
        print(f'Saved snapshot to {snapshot_path}')

    def log(self, mode: str, result: Dict[str, torch.Tensor], batch: Dict[str, torch.Tensor], loss: torch.Tensor,
            global_step: int) -> None:
        if mode != 'train' and mode != 'val':
            raise ValueError('mode must be either train or val')
        print(f'Iteration: {global_step}, {mode} loss: {loss}')
        for metric in self.metrics:
            metric_name = metric.__class__.__name__
            metric_value = metric(result, batch)
            self.writer.add_scalars(metric_name, {mode: metric_value}, global_step)
            print(f'Iteration: {global_step}, {mode} {metric_name}: {metric_value}')
        self.writer.add_scalars("Loss", {'train': loss}, global_step)

    def _train_iteration(self, model: nn.Module, batch: Dict[str, torch.Tensor],
                         global_step: int) -> None:
        model.train()
        self.optimizer.zero_grad()
        result = model(batch)
        loss = self.loss(result, batch)
        loss.backward()
        self.optimizer.step()

        if global_step % self.show_iters == 0:
            self.log('train', result, batch, loss, global_step)

    def _val_iteration(self, model, batch) -> Dict[str, torch.Tensor]:
        model.eval()
        with torch.no_grad():
            result = model(batch)
            loss = self.loss(result, batch)
        return {'loss': loss.item()}

    def _train_loop(self, model, train_loader, val_loader, start_iteration, max_iteration, lr_policy):
        iteration = start_iteration
        while iteration < max_iteration:
            for batch in train_loader:
                self._train_iteration(model, batch, iteration)
                iteration += 1
                if iteration % self.train_iters == 0:
                    self._save_snapshot(model, f'{self.snapshot_dir}/snapshot_{iteration}.pth', iteration)
                if iteration % self.val_iters == 0:
                    self._val_loop(model, val_loader, iteration)
                if iteration == max_iteration:
                    break
            if lr_policy is not None:
                lr_policy.step()

    def _val_loop(self, model, val_loader, iteration):
        losses = []
        for batch in val_loader:
            loss = self._val_iteration(model, batch)
            losses.append(loss)
        mean_loss = sum(losses) / len(losses)
        self.writer.add_scalars("Loss", {'val': mean_loss}, iteration)
        print(f'Validation iteration: {iteration}, mean loss: {mean_loss}')

