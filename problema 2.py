import numpy as np
import matplotlib.pyplot as plt

N = 20 #numero de intervalos
kfinal = 50 #passos no tempo
L = 1 #tamanho da barra
x = np.linspace(0.0, L, N+1) #Vetor x, usado para plotar
deltax = L/N
deltat = 0.2*deltax*deltax
Temp = np.zeros(N+1, float)
Temp[0] = 1.0
Temp[-1] = 0.0
Tempnova = np.copy(Temp)

for k in range (1, kfinal+1):
    for i in range (1, N) :
        Tempnova[i] = Temp[i]+(deltat/(deltax*deltax))*(Temp[i+1]-2.0*Temp[i]+Temp[i-1])
    Temp = np.copy(Tempnova)

t = k*deltat #Tempo atual, usado no titulo do grafico
fig = plt.figure( )
ax = fig.add_subplot( )
fig.suptitle('t = %.3f' %t,fontsize=18, fontweight='bold')
ax.set_ylabel('$T$',fontsize= 18)
ax.set_xlabel('$x$',fontsize=18)
plt.plot(x,Temp,'-r',lw=4)
#plt.savefig('figura.pdf',format='pdf',dpi =1200,bbox_inches='tight')
plt.show()