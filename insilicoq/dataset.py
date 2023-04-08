import os
import urllib
import pandas as pd

# return data frame for diffrent datasets currently 'zinc, 'qm9'
class Dataset:


  def __init__(self):
    self.qm9_url = 'https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/qm9.csv'
    self.zinc_url = 'https://raw.githubusercontent.com/aspuru-guzik-group/chemical_vae/master/models/zinc_properties/250k_rndm_zinc_drugs_clean_3.csv'

  def get(self, dataset):
    if dataset == 'qm9':
      urllib.request.urlretrieve(self.qm9_url, 'qm9.csv')

    if dataset == 'zinc':
      urllib.request.urlretrieve(self.zinc_url,'zinc.csv')

    df = pd.read_csv(f'{dataset}.csv')

    return df
