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

i=np.array(i)
x=[]
for aux in theta:
    x.append(math.tan(math.radians(aux)) /(8*1000000))


linegress.lineregression(x,i)
