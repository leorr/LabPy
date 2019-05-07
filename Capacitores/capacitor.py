#  dados:
#           |    |       
#           | -> |
#   +_______| -> |________-
#           | -> |
#           | -> |
#           |    |
#   Sendo a capacitância de um capacitor:
#   C = eo * A / d

import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import stats
import linegress

c=[]
d=[]

with open('dados.tsv','r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        c.append(float(row[0]))
        d.append(float(row[1]))

c=np.array(c)
d=np.array(d)
tc=np.float_power(10,-12)
tid=np.float_power(10,-3)
x=(1/d)*tid
y=c * tc
linegress.lineregression(x,y)
