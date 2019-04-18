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
