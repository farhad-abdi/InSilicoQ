# Classical neural networks for using in hybrid setting (GAN, CNN, ..)

# import the necessary packages
import torch
import torch.nn as nn
import torch.optim as optim


class ClassicNet(nn.Module):
  
  def __init__(self, net_type:str, input_size:int):
    super().__init__()
    
    self.type = net_type #net type to be created
    self.input_size = input_size
    
    #example discremiator parameters
    self.linear_input = nn.Linear(input_size, 20)
    self.leaky_relu = nn.LeakyReLU(0.2)
    self.linear20 = nn.Linear(20, 1)
    self.sigmoid = nn.Sigmoid()
    
    
    
    
  def forward(self):
    if self.type = 'Discriminator':   
      x = self.linear_input(input)
      x = self.leaky_relu(x)
      x = self.linear20(x)
      x = self.sigmoid(x)
      return x
