import os

from experiments.DDRNet.run_base import RunBase
from optim_utils.iter_policy.linear_policy import LinearIterationPolicy


class Phase(RunBase):
    def __init__(self):
        super().__init__(os.path.abspath(__file__))

        self.optimizer_kwargs = {'lr': 0., 'weight_decay': 3e-5}
        self.lr_policy = LinearIterationPolicy(start_iter=20000, start_lr=3e-3, end_lr=40000, end_val=6e-3)


if __name__ == '__main__':
    Phase().train(start_snapshot=None)