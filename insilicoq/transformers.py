"""
Extract embedding from pretrained transformers on protien sequences(ProtoT5, ProtoBert, ESM, ... )
"""

from transformers import T5EncoderModel, T5Tokenizer
from transformers import AutoTokenizer, AutoModel, AutoConfig

import esm

import torch
import torch.nn as nn


class Embedding(nn.Module):
  
  def __init__(self, model_type:str, input_seq:str):
    self.model_type = model
    self.seq = input_seq
    
    if self.model_type == 'ProtoT5':
      tokenizer = T5Tokenizer.from_pretrained('Rostlab/prot_t5_xl_bfd', do_lower_case=False)
      model = T5Model.from_pretrained("Rostlab/prot_t5_xl_bfd")
      
    if self.model_type == 'ProtoBert':
      tokenizer = #
      model = #
      
    if self.model_type == 'ESM':
      !pip install fair-esm
      tokenizer = #
      model = #
      
    self.input_ids = #
    self.attention_mask,decoder = #
    self.decoder_input_ids = #
      
      
  def forward(self):
    embedding = model(input_ids=input_ids,attention_mask=attention_mask,decoder_input_ids=decoder_input_ids)
    
    
    return embedding
      
      
