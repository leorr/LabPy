import linegress
import csv
import numpy as np
import math
from uncertainties import ufloat
import matplotlib.pyplot as plt
import statistics

p=(1.01*100000-(1.21*9.8*658))*10000
d=[]
with open('dados.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        d.append(float(row[0]))
 
x=[]
v=[]
dn=[]
e=[]
qmax=[]
for i in range(10):
    x.append(293*p*d[i]*10/(760*298.15*1000))
    v.append(24.22*x[i]+6.08*math.pow(x[i],0.5))
    dn.append((d[i]+10)/100)
    e.append(v[i]/dn[i])
    qmax.append(0.1*0.1*e[i]*4*math.pi*8.85/1000000000000)

print(statistics.mean(qmax))
print(statistics.mean(v))
print(statistics.mean(e))
