#   dados:
#
#    ____(R)_____(led)___
#   |          |         |
#   |          |__(V)____|_
#   |                      |
#   |                      |
#   |                      |
#   |_____(i)__+<VD>-______|
#
#   kirchhoff: vd = R*i + v
#   devemos então estimar R com essas informações
#   no nosso caso R é suposto como desconhecido
#   então       vd(R)=i*(R) + v

import matplotlib.pyplot as plt
import csv
import numpy as np

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

y=i
x=vd-v

r= np.polyfit(x,y,1,full=True)    #regressao linear
ranger =np.arange(min(x)-3,max(x)+3.1,0.01) #elaborando um range para exibição 
ry=np.polyval(r[0],x)


fig = plt.figure()
ax = fig.add_subplot(111)



plt.axhline(0, color='black')               #
plt.axvline(0, color='black')               #desenhando as origens

ax.plot(x,y,'.',label='pontos obtidos')
ax.plot(ranger,np.polyval(r[0],ranger),label='linha de regressão')

for i in range(0,np.size(x),1):
    duple = [x[i],x[i]],[y[i],ry[i]]
    ax.plot(duple[0],duple[1],color='red')

ax.set_aspect(1)
plt.legend()
plt.xlim(-2,max(max(x),max(y)))
plt.ylim(-2,max(max(x),max(y)))
plt.grid()
plt.show()


