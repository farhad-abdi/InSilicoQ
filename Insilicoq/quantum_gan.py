import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
# Importing qiskit machine learning parameters
from qiskit.circuit import Parameter, ParameterVector

from qiskit.circuit.library import TwoLocal


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


