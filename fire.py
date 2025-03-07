import matplotlib.pyplot as plt
import numpy as np
import random as ran
import math

max = 1000
l = 100
rot = 50
br = 1
sig = 1
burn_time = 20


class floor():
    def __init__(self):
        self.wood = 0
        self.prob = 0
        self.f = 0
        self.check = 0
        self.edge = 0
        self.sum = 0
    def add(self):
        if (self.edge == 1):
            self.wood = 0
        else:
            self.wood = 1
    def fire(self):
        if (self.wood == 0):
            self.f = 0
        if (self.f == 0 and self.wood > 0):
            self.check=burn_time
            self.f=1
    def update(self):
        if (self.f == 1 and self.check > 1):
            self.check-=1
        if (self.check == 1):
            self.f = 0
            self.wood = 0
            self.check = 0
        if (self.f == 0 and self.sum > 0):
            if (self.sum > abs(ran.gauss(0,sig))):
                self.fire()
            self.sum = 0
            

x = np.empty(shape=(l,l),dtype=np.dtype(floor))
i = 0
while i < l:
    j = 0
    while j < l:
        if (i == 0 or i == l-1 or j == 0 or j == l-1):
            x[i,j] = floor()
            x[i,j].edge = 1
        else:
            x[i,j] = floor()
        j+=1
    i+=1

def add():
    x_i = ran.randint(0,l-1)
    y_i = ran.randint(0,l-1)
    x[x_i,y_i].add()

def check():
    i = 1
    while i < l-1:
        j = 1
        while j < l-1:
            a = -1
            while a < 2:
                b = -1
                while b < 2:
                    if (a == 0 and b == 0):
                        b+=1
                    else:
                        x[i,j].sum += x[i+a,j+b].f
                        b+=1
                a+=1
            j+=1
        i+=1

for r in range(max):
    print(r)
    t = np.zeros(shape=(l,l))
    for z in range(rot):
        add()
    for z in range(br):
        x[ran.randint(0,l-1),ran.randint(0,l-1)].fire()
    check()
    for u in range(l):
        for v in range(l):
            t[u,v] = x[u,v].f
            x[u,v].update()
    if (r%3 == 0):
        plt.imshow(t)
        plt.pause(0.01)
plt.show()