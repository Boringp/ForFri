from card import *
from Player import *
from  GameDealer import *

c=deck()
c.shuffle()
h1=Hand()
h1.get(c,7)
print(h1)
print(h1.getValue())










