import os
import urllib
import pandas as pd

# return data frame for diffrent datasets currently 'zinc, 'qm9'
class Dataset:
  
  @staticmethod
  def get(dataset):
    qm9_url = 'https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/qm9.csv'
    zinc_url = 'https://raw.githubusercontent.com/aspuru-guzik-group/chemical_vae/master/models/zinc_properties/250k_rndm_zinc_drugs_clean_3.csv'

    if dataset == 'qm9':
      urllib.request.urlretrieve(qm9_url, 'qm9.csv')

    if dataset == 'zinc':
      urllib.request.urlretrieve(zinc_url,'zinc.csv')

    df = pd.read_csv(f'{dataset}.csv')

    return df
