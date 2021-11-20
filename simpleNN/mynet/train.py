"""
Here is a function that can train a neural net.
"""

from mynet.tensor import Tensor
from mynet.nn import NeuralNet
from mynet.loss import Loss, MSE
from mynet.optm import Optimizer, SGD
from mynet.dataset import DataIterator, BatchIterator

def train(net: NeuralNet,
            inputs: Tensor,
            targets: Tensor,
            num_epochs: int = 5000,
            iterator: DataIterator = BatchIterator(),
            loss: Loss = MSE(),
            optimizer: Optimizer = SGD()) -> None:
    
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for batch in iterator(inputs, targets):
            predicted = net.forward(batch.inputs)
            epoch_loss += loss.loss(predicted, batch.targets)
            grad = loss.grad(predicted, batch.targets)
            net.backward(grad)
            optimizer.step(net)
        print("epoch:", epoch, "loss:", epoch_loss)
        # if epoch_loss < 1:
        #     return
