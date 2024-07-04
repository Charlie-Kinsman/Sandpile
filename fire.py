import matplotlib.pyplot as plt
import numpy as np
import random as r
import math

max = 200
l = 50
x = np.zeros(shape=(l,l))

class floor():
    def __init__(self):
        self.height = 0
        self.prob = 0
        self.fire = 0
    def add(self):
        self.height+=1

here = floor()
print(here.height)
here.add()
print(here.height)