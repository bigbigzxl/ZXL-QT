from typing import Callable, List, NamedTuple

import numpy as np


class Dependency(NamedTuple):
    tensor: 'Tensor'
    grad_fn: Callable[[np.ndarray], np.ndarray]

class Tensor:
    def __init__(self,
                data: np.ndarray,
                requires_grad: bool == False,
                depends_on: List[Dependency] = None) -> None:
        self.data = data
        self.requires_grad = requires_grad
        self.depends_on = depends_on
        self.shape = data.shape

    def __repr__(self) -> str:
        return f"Tensor({self.data}, requires_ragd={self.requires_grad})"

    def sum(self) -> 'Tensor':
        return tensor_sum(self)

def tensor_sum(t: Tensor) -> Tensor:
    """
    Takes a tensor and returns the 0-tensor
    that's the sum of all it's elements.
    """
    data = t.data.sum()
    requires_grad = t.requires_grad

    if requires_grad:
        def grad_fn(grad: np.ndarray) -> np.ndarray:
            """
            grad is necessarily a 0-tensor, so each input element
            contributes that much
            """
            return grad * np.ones_like(t.data)

        depends_on = [Dependency(t, grad_fn)]
    else:
        depends_on = None

    return Tensor(data,
                requires_grad,
                depends_on)
    