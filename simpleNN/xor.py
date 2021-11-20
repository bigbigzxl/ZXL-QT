"""
The cannonical example of a function that can't be 
learned with a simple linear model is XOR.
"""

import numpy as np

from mynet.train import train
from mynet.nn import NeuralNet
from mynet.layers import Linear, Tanh
from mynet.optm import SGD
inputs = np.array(
    [
        [0,0],
        [1,0],
        [0,1],
        [1,1]
    ]
)

targets = np.array(
    [
        [1,0],
        [0,1],
        [0,1],
        [1,0]
    ]
)

net = NeuralNet(
    [
        Linear(input_size=2, output_size=2),
        Tanh(),
        Linear(input_size=2, output_size=2)
    ]
)

train(net, 
    inputs, 
    targets,
    num_epochs=5000,
    optimizer=SGD(lr=0.03))

for x, y in zip(inputs, targets):
    predicted = net.forward(x)
    print("Input:",x," Predicted:", predicted, " GroundTruth:",y)