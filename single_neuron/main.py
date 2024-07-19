import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    preact = [dot(weights, input_vec) + bias for input_vec in features]
    probabilities = [sigmoid(x) for x in preact]

    mse = (1 / len(features)) * sum((probabilities[i] - labels[i]) ** 2 for i in range(len(features)))

    return probabilities, mse

print(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))