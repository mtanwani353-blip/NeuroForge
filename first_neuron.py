
import numpy as np

def relu(z):
    return max(0, z)

def artificial_neuron(inputs, weights, bias):
    inputs = np.array(inputs, dtype=float)
    weights = np.array(weights, dtype=float)

    if inputs.shape != weights.shape:
        raise ValueError("Inputs and weights must have the same shape.")

    weighted_sum = np.dot(inputs, weights) + bias
    output = relu(weighted_sum)

    return weighted_sum, output


# Example neuron
weights = [0.5, 0.8, 0.2]
bias = 0.1

test_inputs = [
    [2.0, 3.0, 4.0],
    [-2.0, -3.0, -4.0],
    [1.0, 1.0, 1.0]
]

for inputs in test_inputs:
    z, output = artificial_neuron(inputs, weights, bias)

    print(f"Inputs: {inputs}")
    print(f"Weighted sum: {z:.2f}")
    print(f"Neuron output: {output:.2f}")
    print()