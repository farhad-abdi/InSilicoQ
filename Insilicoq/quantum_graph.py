""" A collection of quantum graph based algorithms, the algorthms are mostly based on Grover Serach algorithm"""

from qiskit import QuantumCircuit



class MST:

    """
    Mininum Spanning Tree Implementation
    
    """
    def __init__(self, num_qubit):
    
    self.num_q = num_qubit
    
    
    def oracle_mst(self):
    
    oracle = QuantumCircuit(self.num_q)
    
    
    return oracle
    
    
    def diffuser_mst(self):
    
    diffuser = QuantumCircuit(self.num_q)
    
    
    return diffuser
    
    
    
    
    
    
    


