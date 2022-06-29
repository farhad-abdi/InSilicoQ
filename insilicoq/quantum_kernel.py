# Quantum Kernel Machine Learning Functions 

import numpy as np

## Utilities
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from typing import Optional, Callable, List, Union
from functools import reduce

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.visualization import *
# Qiskit imports 
from qiskit import BasicAer
from qiskit.circuit.library import ZZFeatureMap, PauliFeatureMap
from qiskit.utils import QuantumInstance, algorithm_globals

#Qiskit Machine Learning imports
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit_machine_learning.datasets import ad_hoc_data

# seed for ramdomization, to keep outputs consistent
seed = 123456

#Quantum Computing Backend used in Quantum Kernels
qcomp_backend = QuantumInstance(BasicAer.get_backend('qasm_simulator'), shots=1024,
                                seed_simulator=seed, seed_transpiler=seed)
                                


"""
The following functions are implementations of ref[2] and the corresponding equations are numberd according to the paper.

"""
def data_map_eq8(x: np.ndarray) -> float:
    """
    Define a function map from R^n to R.

    Args:
        x: data

    Returns:
        float: the mapped value
    """
    coeff = x[0] if len(x) == 1 else reduce(lambda m, n: np.pi*(m * n), x)
    return coeff

def data_map_eq9(x: np.ndarray) -> float:
    coeff = x[0] if len(x) == 1 else reduce(lambda m, n: (np.pi/2)*(m * n), 1 - x)
    return coeff

def data_map_eq10(x: np.ndarray) -> float:
    coeff = x[0] if len(x) == 1 else reduce(lambda m, n: np.pi*np.exp(((m - n)*(m - n))/8), x)
    return coeff

def data_map_eq11(x: np.ndarray) -> float:
    coeff = x[0] if len(x) == 1 else reduce(lambda m, n: (np.pi/3)*(m * n), 1/(np.cos(x)))
    return coeff

def data_map_eq12(x: np.ndarray) -> float:
    coeff = x[0] if len(x) == 1 else reduce(lambda m, n: np.pi*(m * n), np.cos(x))
    return coeff
    
    
    

#Define Quantum Kernels Functions

def qkern_default():
    qfm_default = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full')

    return  QuantumKernel(feature_map=qfm_default, quantum_instance=qcomp_backend)

def qkern_eq8():
    qfm_eq8 = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full', data_map_func=data_map_eq8)

    return  QuantumKernel(feature_map=qfm_eq8, quantum_instance=qcomp_backend)

def qkern_eq9():
    qfm_eq9 = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full', data_map_func=data_map_eq9)

    return  QuantumKernel(feature_map=qfm_eq9, quantum_instance=qcomp_backend)

def qkern_eq10():
    qfm_eq10 = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full', data_map_func=data_map_eq10)

    return  QuantumKernel(feature_map=qfm_eq10, quantum_instance=qcomp_backend)

def qkern_eq11():
    qfm_eq11 = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full', data_map_func=data_map_eq11)

    return  QuantumKernel(feature_map=qfm_eq11, quantum_instance=qcomp_backend)

def qkern_eq12():
    qfm_eq12 = PauliFeatureMap(feature_dimension=2, 
                                    paulis = ['ZI','IZ','ZZ'],
                                 reps=2, entanglement='full', data_map_func=data_map_eq12)

    return QuantumKernel(feature_map=qfm_eq12, quantum_instance=qcomp_backend)