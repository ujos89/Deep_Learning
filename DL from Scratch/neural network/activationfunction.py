import numpy as np

# activation function non-linear function

def step_fucntion(x):
    return (x > 0).astype(np.int)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))