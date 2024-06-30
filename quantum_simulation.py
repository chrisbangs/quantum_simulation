import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# Define the quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate to put qubit in superposition
qc.measure(0, 0)

# Simulate the circuit without observation
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
plt.show()

# Analyze the resource usage
# (In a real study, this would involve detailed metrics on computational resources)
print("Resource usage for unobserved simulation:", counts)
