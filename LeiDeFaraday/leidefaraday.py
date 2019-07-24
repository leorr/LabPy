import linegress
import csv
import numpy as np
import math
from uncertainties import ufloat
import matplotlib.pyplot as plt

f = []
vms = []
vmr = []

with open('data.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        f.append(float(row[0]))
        vmr.append(float(row[2]))
        vms.append(float(row[1]))
i = []
Y=[]
w=[]

for aux in range(10):
    i.append(vmr[aux]/22)
    Y.append(vms[aux]/i[aux])
    w.append(2*math.pi*f[aux])

#fazer a propagação de erros
Rs=ufloat(22,(22*5/100))
dY=[]

for aux in range(10):
    dvmr=ufloat(vmr[aux],(vmr[aux]*3/100)+0.1)
    di=dvmr/Rs
    dvms=ufloat(vms[aux],(vms[aux]*3/100)+0.005)
    dY.append((dvms/di).s)
 #   print("dmvr ",dvmr)
  #   print("di ",di)
   #   print(dY[aux])
    

#temos em dzz o erro de z^2, vai ser util para plotagem da linha de erros
#z^2=r^2+(lw)^2
#adiconar plot da barra de erros
ye=linegress.lineregression(w,Y)
plt.plot(w,Y,'.',label='pontos obtidos',color='magenta')
plt.plot(w,ye,label='linha de regressão')
plt.errorbar(w, Y, yerr=dY,label='barra de erros')
#for aux in range(9):
#    plt.plot(zz[aux]-dzz[aux],ye[aux],label='kkkk')

plt.legend()
plt.show()
