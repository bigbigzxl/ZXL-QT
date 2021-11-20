"""
neural nets will be masd up of layers.
Each layer needs to pass its input forward
and propagate gradients backward.
for example, a neural net might look like:
    inputs -> Linear -> Tanh -> Linear -> output
"""
import os, sys

from mynet import tensor
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from typing import Dict, Callable

import numpy as np

from mynet.tensor import Tensor


class Layer:
    def __init__(self) -> None:
        self.params: Dict[str, Tensor] = {}
        self.grads: Dict[str, Tensor] = {}

    def forward(self, inputs: Tensor) -> Tensor:
        """
        Produce the outputs corresponding to these inputs.
        """
        raise NotImplementedError

    def backward(self, grad: Tensor) -> Tensor:
        """
        Backpropagate this gradient through the layer.
        """
        raise NotImplementedError

class Linear(Layer):
    """
    compute output = inputs @ w + b
    """

    def __init__(self, input_size: int, output_size: int) -> None:
        # inputs will be (batch_size, input_size)
        # outputs will be (batch_size, output_size)
        super().__init__()
        self.params['w'] = np.random.randn(input_size, output_size)
        self.params['b'] = np.random.randn(output_size)

    def forward(self, inputs: Tensor) -> Tensor:
        """
        outputs = inputs @ w + b
        """
        self.inputs = inputs
        return inputs @ self.params['w'] + self.params['b']

    def backward(self, grad: Tensor) -> Tensor:
        """
        eltwise-MUL
        if y  = f(x) and x = t * w + b
        then:
                dy/dt = f'(x) * w
                dy/dw = f'(x) * t 
                dy/db = f'(x)

        Matmul
        if y = f(x) and x = t @ w + b
        then:
                dy/dt = f'(x) @ w.T
                dy/dw = t.T @ f'(x)
                dy/db = f'(x)
        """

        self.grads['b'] = np.sum(grad, axis=0) # axis0: batch
        self.grads['w'] = self.inputs.T @ grad
        return grad @ self.params['w'].T


################################################################
F = Callable[[Tensor], Tensor]

class Activation(Layer):
    """
    An activation layer just applies a function
    elementwise to its inputs.
    """
    def __init__(self, f: F, f_prime: F) -> None:
        super().__init__()
        self.f = f
        self.f_prime = f_prime

    def forward(self, inputs: Tensor) -> Tensor:
        self.inputs = inputs
        return self.f(inputs)

    def backward(self, grad:Tensor) -> Tensor:
        """
        if y = f(x) and x = g(t)
        then:
            dy/dz = f'(x) * g'(t)
        """
        return self.f_prime(self.inputs) * grad

def tanh(x: Tensor) -> tensor:
    return np.tanh(x)

def tanh_prime(x: Tensor) -> Tensor:
    y = tanh(x)
    return 1 - y**2

class Tanh(Activation):
    def __init__(self):
        super().__init__(tanh, tanh_prime)
        
