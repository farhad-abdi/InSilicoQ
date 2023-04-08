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
 
def amplitude_encoding(data):
  
  '''
  Args:
  data: 1D numpy array
  
  Return:
  Quantum Circ
  '''
  
  cof = np.sum(np.power(data,2))
  state = (1/np.sqrt(cof)) * data
  num_qubit = int(math.log2(len(data)))
  #how many time decopose trail and error!?
  decompose_time = len(data)
  
  circ = QuantumCircuit(num_qubit)
  print(list(np.arange(num_qubit)))
  circ.prepare_state(state, list(np.arange(num_qubit)))
  circ = circ.decompose(reps = decompose_time)
 
  return circ
 
 
 
 
