# NeuroForge

An educational neural-network framework built from scratch using Python and NumPy.

## Phase 1: First Artificial Neuron

### Objective
Understand and implement the forward calculation of a single artificial neuron.

### Concepts implemented
- Inputs, weights, and bias
- Weighted sum using NumPy's dot product
- ReLU (Rectified Linear Unit) activation
- Reusable neuron function
- Input and weight shape validation
- Testing with multiple input combinations


### Core calculation

1. Weighted Sum = (Input 1 × Weight 1) + (Input 2 × Weight 2) + ... + Bias
2. Neuron Output = ReLU(Weighted Sum)
3. ReLU(z) = max(0, z)

ReLU returns 0 when the weighted sum is negative.
Otherwise, it returns the weighted sum unchanged.

### Example

Inputs: `[2.0, 3.0, 4.0]`

Weights: `[0.5, 0.8, 0.2]`

Bias: `0.1`

Expected weighted sum: `4.3`

Expected ReLU output: `4.3`

### Current limitations
The neuron uses manually specified weights and bias. It performs a forward calculation but does not train itself or learn from data.

### Next milestone
Build on this foundation by introducing training data, target values, and a loss function.

## Project status

Phase 1 — First artificial neuron: implementation and testing completed, pending final understanding review and documentation verification.
