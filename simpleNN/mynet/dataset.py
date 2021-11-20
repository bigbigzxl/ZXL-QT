"""
I will feed inouts into my network in batchs.
So here are some tools for iterating over data in batchs.
"""

from typing import Iterator, NamedTuple
import numpy as np

from mynet.tensor import Tensor


Batch = NamedTuple("Batch", [("inputs", Tensor), ("targets", Tensor)])

class DataIterator:
    def __call__(self, inputs: Tensor, target: Tensor) -> Iterator[Batch]:
        raise NotImplementedError

class BatchIterator(DataIterator):
    def __init__(self, batch_size: int = 32, shuffle: bool = False) -> None:
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __call__(self, inputs: Tensor, target: Tensor) -> Iterator[Batch]:
        starts = np.arange(0, len(inputs), self.batch_size)
        
        if self.shuffle:
            np.random.shuffle(starts)
        
        for start in starts:
            end = start + self.batch_size
            batch_inputs  = inputs[start:end]
            batch_targets = target[start:end]
            yield Batch(batch_inputs, batch_targets) 