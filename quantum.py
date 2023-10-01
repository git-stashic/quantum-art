from qiskit import transpile, QuantumCircuit
from qiskit_aer import AerSimulator
import random


backend = AerSimulator()

sounds = {'0000': 'C', '0001': 'Cis', '0010': 'D',  '0011': 'Dis', '0100': 'E',
          '0101': 'F', '0110': 'Fis', '0111': 'G',  '1000': 'Gis', '1001': 'A',
          '1010': 'Ais', '1011': 'B',  '1100': '*', '1101': '/', '1110': '_', '1111':  '/'}

special = ['/', '*']

def apply_random_gate(qc, qubit, other_qubits):
    gate_choice = random.choice(['H', 'X', 'Y', 'Z', 'CX', 'RY', 'RZ'])

    if gate_choice == 'H':
        qc.h(qubit)
    elif gate_choice == 'X':
        qc.x(qubit)
    elif gate_choice == 'Y':
        qc.y(qubit)
    elif gate_choice == 'Z':
        qc.z(qubit)
    elif gate_choice == 'CX':
        control = random.choice(other_qubits)
        qc.cx(control, qubit)
    elif gate_choice == 'RY':
        angle = random.uniform(0, 2 * 3.14159)
        qc.ry(angle, qubit)
    elif gate_choice == 'RZ':
        angle = random.uniform(0, 2 * 3.14159)
        qc.rz(angle, qubit)

def generate_circuit(qc):
    for _ in range(5):
        target_qubit = random.choice([0, 1, 2, 3])
        other_qubits = [q for q in [0, 1, 2, 3] if q != target_qubit]
        apply_random_gate(qc, target_qubit, other_qubits)

    return qc


def get_value(circ):
    # Measurement
    meas = QuantumCircuit(4, 4)
    meas.barrier(range(4))
    meas.measure(range(4), range(4))
    qc = meas.compose(circ, range(4), front=True)
    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=1)
    return sounds[list(job_sim.result().get_counts(qc_compiled).keys())[0]]


def run_tact():
    position = 0
    sounds = []

    qc = QuantumCircuit(4,4)

    while (position <= 7):
        sound_1 = get_value(generate_circuit(qc))
        sound_2 = get_value(generate_circuit(qc))
        if (sound_1 in special):
            continue

        if (sound_2 == "*" and position > 4):
            continue

        if (position == 7):
            sounds.append(sound_1 + '/')
            position += 1
            break

        if (sound_2 == "*"):
            sounds.append(sound_1 + '*')
            position += 4
            continue

        if (sound_2 == "/"):
            sounds.append(sound_1 + '/')
            position += 1
            continue

        if (position > 4):
            sounds.append(sound_1)
            position += 2
            continue

        sounds.append(sound_1)
        sounds.append(sound_2)
        position += 4

    return sounds


def create_song(length):
    tacts = []
    for i in range(length):
        tacts.append(run_tact())
    return tacts