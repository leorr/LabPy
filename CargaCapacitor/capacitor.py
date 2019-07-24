import linegress
import csv
import numpy as np
import math
from uncertainties import ufloat
from uncertainties import umath
import matplotlib.pyplot as plt

t=[]#ms
lnv=[]
tau=47*47/100000

with open('dadosdescarga.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        t.append(float(row[0]))
        lnv.append(float(row[1]))

y=[]
dy=[]
for i in range(10):
    dd=ufloat(lnv[i],(lnv[i])*4/100+0.5001)
    dy.append(umath.log(math.fabs((dd).s)))
    y.append(lnv[i])

ye=linegress.lineregression(t,y)

#for i in range(10):
#    print(math.log(v0-v[i]))

plt.plot(t,y,'.',label="pontos obtidos experimentalmente",color='grey')
plt.plot(t,ye,label='regressao')
plt.errorbar(t, y, yerr=dy,label='barra de erros')
plt.legend()
plt.show()
