import matplotlib.pyplot as plt
import csv
import numpy as np


#importando os dados
x=[]
y=[]
V=[]

with open('data_puntiforme.tsv','r') as tsvfile:
    plots = csv.reader(tsvfile, delimiter='\t')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        V.append(float(row[2]))


#preparando a regrssão

c1=np.polyfit(x[:5],y[:5],2)
c2=np.polyfit(x[6:14],y[6:14],2)
c3=np.polyfit(x[15:23],y[15:23],2)
c4=np.polyfit(x[24:32],y[24:32],2)
c5=np.polyfit(x[33:41],y[33:41],2)


range = range =np.arange(min(x),max(x),0.01)

plt.plot(    
    x,y,'.',label='dados obtidos experimentalmente'
)

plt.plot(
        range,np.polyval(c1,range),
    label='curva de regressão 1V'
    )
plt.plot(

    range,np.polyval(c2,range), 
    label='curva de regressão 2V'
    )
plt.plot(
        
    range,np.polyval(c3,range), 
    label='curva de regressão 2.5V'

    )
plt.plot(   
    range,np.polyval(c4,range), 
    label='curva de regressão 3V'

    )
plt.plot(
    range,np.polyval(c5,range), 
    label='curva de regressão 4V'
)

plt.legend()
plt.xlim(min(x)-0.1,max(x)+0.1)
plt.ylim(min(y),max(y)+0.1)
