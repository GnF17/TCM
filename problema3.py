import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

N = 20 #numero de intervalos
kfinal = 10 #passos no tempo
L = 2 #tamanho da barra
x = np.linspace(0.0, L, N+1) #Vetor x, usado para plotar
deltax = L/N
deltat = 0.2*deltax*deltax
Temp = []

def ssin(x): return sp.N(sp.sin(x))

for i in range(int(N+1)):
    Temp.append(ssin((sp.pi*float(deltax*i))/2))
    if ssin((sp.pi*float(deltax*i))/2)<0.000001:
        Temp[i]=0.0
print(Temp)

Tempnova = np.copy(Temp)


for k in range (1, kfinal+1):
    for i in range (1, int(N)) :
        Tempnova[i] = Temp[i]+(deltat/(deltax*deltax))*(Temp[i+1]-2.0*Temp[i]+Temp[i-1])
    Temp = np.copy(Tempnova)

t = k*deltat #Tempo atual, usado no titulo do grafico
fig = plt.figure( )
ax = fig.add_subplot( )
fig.suptitle('t = %.3f' %t,fontsize=18, fontweight='bold')
ax.set_ylabel('$T$',fontsize= 18)
ax.set_xlabel('$x$',fontsize=18)
plt.plot(x,Temp,'-r',lw=4)
plt.savefig('figura.png',format='png',dpi =1200,bbox_inches='tight')
plt.show()