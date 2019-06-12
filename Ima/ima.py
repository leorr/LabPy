import linegress
import csv
import numpy as np
import math

i = []
theta = []

with open('dados.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        i.append(float(row[0]))
        theta.append(float(row[1]))

x=[]
for aux in theta:
    x.append(math.tan(math.radians(aux)))
#uo = 4 * l pi 10^-7



# i = Bt * (pi*L / 2*u0) * x
# Bt = (i * 8 * 10^-7) / (L*x)

bt=[]

for aux in range(20):
    bt=i[aux]*8*0.0000001/ (0.0724  * x[aux])

print(bt)

linegress.lineregression(x,i)
