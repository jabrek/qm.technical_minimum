# Wymaga: pip install qiskit qiskit-aer
# https://quantum.cloud.ibm.com/docs/en/guides/quick-start
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def useStateVectorSampler(qc):
    simulator = StatevectorSampler()
    job = simulator.run(qc)


def useAerSimulator(qc):
    # 4. Tworzymy simulator
    simulator = AerSimulator()

    # 5. Kompilujemy obwód dla symulatora
    compiled_circuit = transpile(qc, simulator)

    # 6. Uruchamiamy obwód na symulatorze
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    return result


# 1. Tworzymy obwód: 1 qubit, 1 bit klasyczny
qc = QuantumCircuit(1, 1)

# 2. Nakładamy bramkę Hadamarda (H) - tworzymy superpozycję
qc.h(0)

# 3. Mierzymy qubit i zapisujemy wynik w klasycznym bicie
qc.measure(0, 0)

# 7. Pobieramy wyniki
result = useAerSimulator(qc)
counts = result.get_counts(qc)
fig = plot_histogram(counts)  # Wyświetlamy histogram wyników
plt.show(block=True)
# wait for user to close the plot
# input("Press Enter to continue...")
# print(f"Wyniki pomiarów: {counts}")
