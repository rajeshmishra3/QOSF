import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Sampler

"""
Input given as past of the task
size = 5
state_values = [22,17,27,12]
state_vector = [0]*2**size

for s in state_values:
    print(np.binary_repr(s,size))
    state_vector[s] = 0.5
"""

qr = QuantumRegister(5)
cr = ClassicalRegister(5)
qc = QuantumCircuit(qr, cr)

# Superposition of q3 and q2
qc.h(2)
qc.h(3)
# qc.barrier()

# q1 = q3 XOR q2
# Swap q1 and q3
qc.cnot(1,3)
qc.cnot(3,1)

qc.cnot(2,3)
# qc.barrier()

# Swap q1 and q3
qc.cnot(3,1)
qc.cnot(1,3)
qc.cnot(3,1)

# q0 = q3 XNOR q2
qc.x(0)
qc.cnot(3,0)
qc.cnot(1,0)
# qc.barrier()

# q4 = q3 NAND q2
qc.x(4)
# Toffoli gate implementation using basis gates
qc.h(4)
qc.cnot(3,4)
qc.rz(-math.pi/4,4)
qc.cnot(2,4)
qc.rz(math.pi/4,4)
qc.cnot(3,4)
qc.rz(-math.pi/4,4)
qc.cnot(2,4)
qc.rz(math.pi/4,4)
qc.rz(math.pi/4,3)
qc.h(4)
qc.cnot(2,3)
qc.rz(-math.pi/4,3)
qc.rz(math.pi/4,2)
qc.cnot(2,3)
qc.barrier()

# measure
qc.measure(qr, cr)

print(qc)

print(qc.depth())

circ_sampler = Sampler()
job = circ_sampler.run(qc)
data = job.result().quasi_dists
print(data)