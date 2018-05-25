# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
index=range(1,len(fx))
index2=range(1,len(fx-1))
h=x[1]-x[0]
df=(fx[1:-1]-fx[0:-2])/(2*h)
d2f=(df[1:-1]-df[1:-1])/(2*h)
plt.plot(x[2:-2],d2f)
plt.savefig('segunda.png')
