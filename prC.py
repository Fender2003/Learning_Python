from qiskit import QuantumCircuit, QuantumRegister, execute, Aer
from qiskit.visualization import plot_histogram

qc_output = QuantumCircuit(8)
print(qc_output) #creating 8 qubits

qc_output.measure_all() #adds measurement to all the qubits

qc_output.draw(initial_state=True)  #draws the circuit
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_output).result()
counts = result.get_counts()
plot_histogram(counts)