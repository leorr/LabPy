import linegress
import csv
import numpy as np
import math
from uncertainties import ufloat
import matplotlib.pyplot as plt

f = []
vml = []
vmr = []

with open('data.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        f.append(float(row[0]))
        vmr.append(float(row[1]))
        vml.append(float(row[2]))
i = []
z = []
zz= []
w = []
ww = []
for aux in range(9):
    i.append(vmr[aux]/22)
    z.append(vml[aux]/i[aux])
    zz.append(z[aux]*z[aux])
    w.append(2*math.pi*f[aux])
    ww.append(w[aux]*w[aux])

#print("(I)",i)
#print("\n--------------\n(Z)",z)
#print("(WW)",ww)
#fazer a propagação de erros
Rs=ufloat(22,(22*5/100))
dzz = []
for aux in range(9):
    dvmr=ufloat(vmr[aux],(vmr[aux]*3/100)+0.1)
    di=dvmr/Rs
    dvml=ufloat(vml[aux],(vml[aux]*3/100)+0.1)
    dz=dvml/di
    dzz.append((dz*dz).s)
#temos em dzz o erro de z^2, vai ser util para plotagem da linha de erros
#z^2=r^2+(lw)^2
#adiconar plot da barra de erros
ye=linegress.lineregression(ww,zz)
plt.plot(ww,zz,'.',label='pontos obtidos',color='magenta')
plt.plot(ww,ye,label='linha de regressão')
plt.errorbar(ww, zz, yerr=dzz,label='barra de erros')
#for aux in range(9):
#    plt.plot(zz[aux]-dzz[aux],ye[aux],label='kkkk')

plt.legend()
plt.show()
