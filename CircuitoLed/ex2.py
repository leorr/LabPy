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
#importando os dados
import linegress
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
linegress.lineregression(x,y)
x=v
linegress.lineregression(x,y)
