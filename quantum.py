from qiskit import transpile, QuantumCircuit
from qiskit_aer import AerSimulator


backend = AerSimulator()

sounds = {'0000': 'C', '0001': 'Cis', '0010': 'D',  '0011': 'Dis', '0100': 'E',
          '0101': 'F', '0110': 'Fis', '0111': 'G',  '1000': 'Gis', '1001': 'A',
          '1010': 'Ais', '1011': 'B',  '1100': '', '1101': '', '1110': '', '1111':  ''}


def get_value(gates_list=[]):
    circ = QuantumCircuit(4,4)
    circ.h(0)
    circ.cx(0, 1)
    circ.cx(0, 2)
    circ.cx(0, 3)

    # Measurement
    meas = QuantumCircuit(4, 4)
    meas.barrier(range(4))
    meas.measure(range(4), range(4))
    qc = meas.compose(circ, range(4), front=True)
    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=1)
    return job_sim.result().get_counts(qc_compiled)

print(get_value())