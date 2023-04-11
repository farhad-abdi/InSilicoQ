import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
# Importing qiskit machine learning parameters
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import TwoLocal

#first net imports
from qiskit import QuantumCircuit
from qiskit.circuit.library import EfficientSU2
from qiskit.primitives import Sampler
from qiskit_machine_learning.connectors import TorchConnector
from qiskit_machine_learning.neural_networks import SamplerQNN

# created quantum neural network in TorchConnector to make use of PyTorch-based training.
def QGenerator(num_qubits) -> TorchConnector:
  
    qc = QuantumCircuit(num_qubits)
    qc.h(qc.qubits)
    ansatz = EfficientSU2(num_qubits, reps=6)
    qc.compose(ansatz, inplace=True)
    
    print(qc.num_parameters)
    
    shots = 10000
    sampler = Sampler(options={"shots": shots, "seed": algorithm_globals.random_seed})
    
    qnn = SamplerQNN(
        circuit=qc,
        sampler=sampler,
        input_params=[],
        weight_params=qc.parameters,
        sparse=False,
    )

    initial_weights = algorithm_globals.random.random(qc.num_parameters)
    return TorchConnector(qnn, initial_weights)




#alternative qgan
class QGAN:
  def __init__(self, num_qubit):
    self.num_q = num_qubit

  def qgenerator(self):
    generator = TwoLocal(self.num_q,
                     # Parameterized single qubit rotations
                     ['ry', 'rz'],
                     'cz',  # Entangling gate
                     'full', # Entanglement structure: all to all
                     reps=2, # Number of layers
                     parameter_prefix='θ_g', 
                     name='Generator')
    generator = generator.decompose() # decompose into standard gates

    return generator

  def qdiscriminator(self):
    disc_weights = ParameterVector('θ_d', 12)

    discriminator = QuantumCircuit(3, name="Discriminator")
    discriminator.barrier()
    discriminator.h(0)
    discriminator.rx(disc_weights[0], 0)
    discriminator.ry(disc_weights[1], 0)
    discriminator.rz(disc_weights[2], 0)

    discriminator.rx(disc_weights[3], 1)
    discriminator.ry(disc_weights[4], 1)
    discriminator.rz(disc_weights[5], 1)

    discriminator.rx(disc_weights[6], 2)
    discriminator.ry(disc_weights[7], 2)
    discriminator.rz(disc_weights[8], 2)
    discriminator.cx(0, 2)
    discriminator.cx(1, 2)
    discriminator.rx(disc_weights[9], 2)
    discriminator.ry(disc_weights[10], 2)
    discriminator.rz(disc_weights[11], 2)

    #discriminator.draw()

    return discriminator

  def qgan_model(self):

    qgan = QuantumCircuit(self.num_q +1 )
    qgan.compose(self.qgenerator(), inplace = True)
    qgan.compose(self.qdiscriminator(), inplace = True)

    return qgan


