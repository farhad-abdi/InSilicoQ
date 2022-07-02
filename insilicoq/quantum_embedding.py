"""
 Quantum Data Encoding Functions: Basis Encoding, Amplitude Encoding, Angle Encoding
 
"""
 
from qiskit import QuantumCircuit
from sklearn.preprocessing import normalize #import normalization function
from qiskit.circuit.library import ZFeatureMap

 

def angle_encoding(num_qubit, data):
    


  '''
  Args:
  num_qubit : number of feature space dimesnion
  data : 1D array real data to be encoded

  Return:
  Quantum Data Circuit Object 
  
  '''
  
  data  = normalize(data)
  feature_map = ZFeatureMap(feature_dimension= num_qubit, reps = 1 )
  data_circ = feature_map.assign_parameters(data[0]/2)

  return data_circ
 
