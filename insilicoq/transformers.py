from transformers import T5EncoderModel, T5Tokenizer
from transformers import AutoTokenizer, AutoModel, AutoConfig

#import esm

import torch
import torch.nn as nn


class Embedding:
  
  def __init__(self, model_type:str):
    

    self.model_type = model_type

    self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    print(f'Running model on {self.device}')

    
    if self.model_type == 'ProtoT5':

      # Loading full percision model requires high ram 24G
      #tokenizer = T5Tokenizer.from_pretrained('Rostlab/prot_t5_xl_bfd', do_lower_case=False)
      #model = T5Model.from_pretrained("Rostlab/prot_t5_xl_bfd")

      #instead loading half percsion model
      self.model = T5EncoderModel.from_pretrained("Rostlab/prot_t5_xl_half_uniref50-enc").to(self.device)
      self.tokenizer = T5Tokenizer.from_pretrained('Rostlab/prot_t5_xl_half_uniref50-enc', do_lower_case=False)
      
    
      
      
  def forward(self, seq):

    token_encoding = self.tokenizer.batch_encode_plus(seq, add_special_tokens=True, padding="longest")
    input_ids      = torch.tensor(token_encoding['input_ids']).to(self.device)
    attention_mask = torch.tensor(token_encoding['attention_mask']).to(self.device)

    with torch.no_grad():

      embedding = self.model(input_ids=input_ids,attention_mask=attention_mask)
    
    
    return embedding
