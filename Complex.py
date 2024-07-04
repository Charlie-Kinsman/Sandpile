import matplotlib.pyplot as plt
import numpy as np
import random as r
import math

max = 200
l = 50
half = int(l/2)
x = np.zeros(shape=(l,l))
freq = []
ind = []

def topple(a,b):
    x[a,b]-=4
    if (a+1 < l):
        x[a+1,b]+=1
    if (b+1 < l):
        x[a,b+1]+=1
    if (a-1 >= 0):
        x[a-1,b]+=1
    if (b-1 >= 0):
        x[a,b-1]+=1



for i in range(max):
    if (i%1 == 0):
        print(i)
    if (i%10 == 0):
        plt.imshow(x)
        plt.pause(0.01)
    x_i = r.randint(0,l-1)
    y_i = r.randint(0,l-1)
    x[half,half]+=1
    f = 0
    if (len(x[x>=4]) > 0):
        s = len(x[x>=4])
        s_i = r.randint(0,s-1)
        d = 0
        indx = []
        indy = []
        for a in range(l):
            for b in range(l):
                if (x[a,b] >= 4):
                    indx.append(a)
                    indy.append(b)
        while (len(x[x>=4]) > 0):
            if (len(indx) == 0):
                break
            if (len(indx)-1 <= 0):
                ch = 0
            else:
                ch = r.randint(0,len(indx)-1)
            topple(indx[ch],indy[ch])
            f+=1
            if (indx[ch]+1 < l):
                if (x[indx[ch]+1,indy[ch]] == 4):
                    indx.append(indx[ch]+1)
                    indy.append(indy[ch])
            if (indy[ch]+1 < l):
                if (x[indx[ch],indy[ch]+1] == 4):
                    indx.append(indx[ch])
                    indy.append(indy[ch]+1)
            if (indx[ch]-1 > 0):
                if (x[indx[ch]-1,indy[ch]] == 4):
                    indx.append(indx[ch]-1)
                    indy.append(indy[ch])
            if (indy[ch]-1 > 0):
                if (x[indx[ch],indy[ch]-1] == 4):
                    indx.append(indx[ch])
                    indy.append(indy[ch]-1)
            indx.pop(ch)
            indy.pop(ch)
    if (f>0):
        freq.append(f)
        ind.append(i)

tot = np.stack((ind,freq),axis=1)
with open('f.npy', 'wb') as f:
    np.save(f, tot)

#plt.imshow(x)
plt.show()
