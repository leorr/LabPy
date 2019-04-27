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


def lineregression(x,y):
    n = np.size(y)                          #tamanho amostral

    ym=0                                    #y medio
    for i in range(0,n):             
        ym=ym+y[i]
    ym=ym/n
    
    xm=0                                    #x medio
    for i in range(0,n):             
        xm=xm+x[i]
    xm=xm/n                                 
                                            
    sxx=0                                   #hipotese(metodo dos mínimos quadrados)
    sxy=0                                   #y = ax + b
    for i in range(0,n):                  #a = sxy/sxx
        sxx=(x[i]-xm)**2 + sxx              #b = ym - a * xm

    for i in range(0,n):
        sxy=(x[i]-xm)*(y[i]-ym) + sxy
    a=sxy/sxx
    b=ym-(a*xm)
    
    ye=[]
    for i in range(0,n):
        ye.append(a*x[i]+b)


    fig = plt.figure()                      
    ax = fig.add_subplot(111)               #preparando plots

    ax.plot(x,y,'.',label='pontos obtidos',color='red')
    ax.plot(x,ye,label='linha de regressão')

    for i in range(0,n):                  #
        res = [x[i],x[i]],[y[i],ye[i]]      #resíduos, xo E yo -> ye  
        ax.plot(res[0],res[1],'--',linewidth=0.5,color='red')     #
    ax.plot(0,0,'--',linewidth=0.5,color='red',label='resíduos')
    plt.errorbar(x,y,0.005,0.0525,fmt='.k',alpha=0.5,label='barra de erros')

    SQres = 0
    for i in range(0,n):
        SQres= (y[i]-ye[i])**2 + SQres

    SQexp = 0
    for i in range(0,n):
        SQexp = (ye[i]-ym)**2 + SQexp

    SQtot = SQexp + SQres 
    R2=SQexp/SQtot
    #chisq=sum((y[i]-ye[i])/si)**2
    stdm=np.std(y)/np.sqrt(n)

    chisq=0
    for i in range(0,n,1):
        chisq=(((y[i]-ye[i])/stdm)**2) + chisq

    c2='χ²=' + str("{:.3f}".format(chisq))           #convertendo chi quadrado para ser mostrado em texto
    R2='R²='+str("{:.3f}".format(R2))#coeficiente de correlação² em texto
    eq='y='+str("{:.2f}".format(a)) + 'x' + str("{:.2f}".format(b))#equaçao da reta tem texto

    plt.axhline(0, color='black')               #
    plt.axvline(0, color='black')               #desenhando as origens
    ax.text(5,3.5,c2)
    ax.text(5,4,R2)
    ax.text(5,4.5,eq)
    ax.set_aspect(1)
    plt.legend()
    plt.xlim(-1,4.85)
    plt.ylim(-1,4.85)
    plt.grid(which='both')
    plt.show()
#FIM DA FUNÇÃO

#importando os dados
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
lineregression(x,y)
x=v
lineregression(x,y)
