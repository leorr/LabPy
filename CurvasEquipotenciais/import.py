import matplotlib.pyplot as plt
import csv
import numpy as np

x=[]
y=[]
V=[]

#importando os dados
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


range =np.arange(min(x)-10,max(x)+10,0.01)
range1 =np.arange(min(x[:5]),max(x[:5]),0.01)
range2 =np.arange(min(x[6:14]),max(x[6:14]),0.01)
range3 =np.arange(min(x[15:23]),max(x[15:23]),0.01)
range4 =np.arange(min(x[24:32]),max(x[24:32]),0.01)
range5 =np.arange(min(x[33:41]),max(x[33:41]),0.01)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(    
    x,y,'.',label='dados obtidos experimentalmente'
)

ax.plot(
    range1,np.polyval(c1,range1),
    label='curva de regressão 1V'
    )
ax.plot(
    range2,np.polyval(c2,range2), 
    label='curva de regressão 2V'
    )
ax.plot(
    range3,np.polyval(c3,range3), 
    label='curva de regressão 2.5V'
    )
ax.plot(   
    range4,np.polyval(c4,range4), 
    label='curva de regressão 3V'
    )
ax.plot(
    range5,np.polyval(c5,range5), 
    label='curva de regressão 4V'
    )
ax.plot(
    range,np.polyval(c1,range),'--',
    range,np.polyval(c2,range),'--',
    range,np.polyval(c3,range),'--',
    range,np.polyval(c4,range),'--',
    range,np.polyval(c5,range),'--',
    alpha=0.2,
    color='black'
    )

ax.set_xlabel('X',rotation=0)
ax.set_ylabel('Y',rotation=0)
ax.set_xticks(np.arange(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5,2))
ax.set_yticks(np.arange(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5,2))
ax.set_aspect(1)
plt.legend()
plt.xlim(min(min(x),min(y))-2,max(max(x),max(y))+2)
plt.ylim(min(min(x),min(y))-2,max(max(x),max(y))+2)
plt.grid()
plt.show()


# dados do experimento da barra
x=[]
y=[]
V=[]
with open('barra.tsv','r') as tsvfile:
    plots = csv.reader(tsvfile, delimiter='\t')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        V.append(float(row[2]))


#preparando a regrssão

c1=np.polyfit(x[:5],y[:5],2)
y1=[i * (-1) for i in y[:5]]
c2=np.polyfit(x[6:14],y[6:14],2)
c3=np.polyfit(x[15:23],y[15:23],2)
c4=np.polyfit(x[24:32],y[24:32],2)
c5=np.polyfit(x[33:41],y[33:41],2)


range =np.arange(min(x)-10,max(x)+10,0.01)
range1 =np.arange(min(x[:5]),max(x[:5]),0.01)
range2 =np.arange(min(x[6:14]),max(x[6:14]),0.01)
range3 =np.arange(min(x[15:23]),max(x[15:23]),0.01)
range4 =np.arange(min(x[24:32]),max(x[24:32]),0.01)
range5 =np.arange(min(x[33:41]),max(x[33:41]),0.01)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(    
    x,y,'.',label='dados obtidos experimentalmente'
)

ax.plot(
    range1,np.polyval(c1,range1),
    label='curva de regressão 1V'
    )
ax.plot(

    range2,np.polyval(c2,range2), 
    label='curva de regressão 2V'
    )
ax.plot(
        
    range3,np.polyval(c3,range3), 
    label='curva de regressão 2.5V'

    )
ax.plot(   
    range4,np.polyval(c4,range4), 
    label='curva de regressão 3V'

    )
ax.plot(
    range5,np.polyval(c5,range5), 
    label='curva de regressão 4V'
)
ax.plot(
    range,np.polyval(c1,range),'--',
    range,np.polyval(c2,range),'--',
    range,np.polyval(c3,range),'--',
    range,np.polyval(c4,range),'--',
    range,np.polyval(c5,range),'--',
    alpha=0.2,
    color='black'
    )


ax.set_aspect(1)

ax.set_xlabel('X',rotation=0)
ax.set_ylabel('Y',rotation=0)
ax.set_xticks(np.arange(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5,2))
ax.set_yticks(np.arange(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5,2))

plt.legend()
plt.ylim(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5)
plt.xlim(min(min(x),min(y))-0.5,max(max(x),max(y))+0.5)
plt.grid(True)
plt.show()


