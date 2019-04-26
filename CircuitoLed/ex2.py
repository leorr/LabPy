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


def pearsonregression(x,y):
    r= np.polyfit(x,y,1,full=True)          #regressao linear
    n = np.size(y)                          #tamanho amostral

    ye=[]                                   #y esperado
    for i in range(0,n,1):             
        ye.append(r[0][0] * x[i] + r[0][1])
    ye=np.array(ye)

    ym=0                                    #y medio
    for i in range(0,n,1):             
        ym=ym+y[i]
    ym=ym/n
    
    xm=0                                    #x medio
    for i in range(0,n,1):             
        xm=xm+x[i]
    xm=xm/n
    

    fig = plt.figure()                      
    ax = fig.add_subplot(111)               #preparando plots

    ax.plot(x,y,'.',label='pontos obtidos',color='red')
    ax.plot(x,ye,label='linha de regressão')

    for i in range(0,n,1):                  #
        res = [x[i],x[i]],[y[i],ye[i]]      #resíduos, xo E yo -> ye  
        ax.plot(res[0],res[1],'--',linewidth=0.5,color='red')     #
    ax.plot(0,0,'--',linewidth=0.5,color='red',label='barras de erro(resíduos)')

    #temos a regressão da reta, b0 e b1 portanto vamos aos testes:
    SQres = 0
    for i in range(0,n,1):
        SQres= (y[i]-ye[i])**2 + SQres

    SQexp = 0
    for i in range(0,n,1):
        SQexp = (ye[i]-ym)**2 + SQexp

    SQtot = SQexp + SQres 
    R2=SQexp/SQtot

    c2='χ²=' + str("{:.3f}".format(stats.chisquare(x,y)[0]))            #convertendo chi quadrado para ser mostrado em texto
    R2='R²='+str("{:.2f}".format(R2))#coeficiente de correlação² em texto
    eq='y='+str("{:.2f}".format(r[0][0])) + 'x+' + str("{:.2f}".format(r[0][1]))#equaçao da reta tem texto


    plt.axhline(0, color='black')               #
    plt.axvline(0, color='black')               #desenhando as origens
    ax.text(max(x)+1,3.5,c2)
    ax.text(max(x)+1,4,R2)
    ax.text(max(x)+1,4.5,eq)
    ax.set_aspect(1)
    plt.legend()
    plt.xlim(-1,4.85)
    plt.ylim(-1,4.85)
    plt.grid(which='both')
    plt.show()
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

y=i#y observado
x=vd-v
pearsonregression(x,y)
x=v
pearsonregression(x,y)
