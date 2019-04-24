#   dados:
#
#    ____(R)_____(led)___
#   |          |         |
#   |          |__(v)____|_____
#   |                          |
#   |                          |
#   |                          |
#   |_____(i)__ + <vd> - ______|
#
#   kirchhoff: vd = R*i + v
#   devemos então estimar R com essas informações
#   no nosso caso R é suposto como desconhecido
#   então       vd(R)=i*(R) + v

import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import stats

vd=[]
i=[]
v=[]

with open('dados.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        vd.append(float(row[0]))
        i.append(float(row[1]))
        v.append(float(row[2]))

vd = np.array(vd)
i = np.array(i)
v = np.array(v)

y=i#y observado
x=vd-v

r= np.polyfit(x,y,1,full=True)    #regressao linear
ry=np.polyval(r[0],x)             #a regressao si é r[0]


fig = plt.figure()
ax = fig.add_subplot(111)
ranger =np.arange(min(x)-3,max(x)+3.1,0.01) #elaborando um range para exibição 
plt.axhline(0, color='black')               #
plt.axvline(0, color='black')               #desenhando as origens

ax.plot(x,y,'.',label='pontos obtidos',color='red')
ax.plot(ranger,np.polyval(r[0],ranger),label='linha de regressão')

for i in range(0,np.size(x),1):             #
    duple = [x[i],x[i]],[y[i],ry[i]]        #resíduos
    ax.plot(duple[0],duple[1],color='red')  #
ax.plot(0,0,color='red',label='barras de erro(resíduos)')


#y esperado
ye=[]
for i in range(0,np.size(x),1):             #
    ye.append(r[0][0] * x[i] + r[0][1])

chi2=stats.chisquare(y,ye,8)[0] #chi quadrado para 8 graus de liberdade

c2='χ²=' + str(chi2)
eq='y='+str("{:.2f}".format(r[0][0])) + 'x' + str("{:.2f}".format(r[0][1]))
R2='R²='+str("{:.2f}".format(stats.linregress(x, y)[2] ** 2))

ax.text(5,3,c2)
ax.text(5,5,eq)
ax.text(5,4,R2)
ax.set_aspect(1)
plt.legend()
plt.xlim(-2,max(max(x),max(y)))
plt.ylim(-2,max(max(x),max(y)))
plt.grid(which='both')
plt.show()
#primeira parte pronta!
#agora falta realizar p y=i x=vd


