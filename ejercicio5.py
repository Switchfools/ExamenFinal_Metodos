# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
sigma = 10
beta=2.67
rho=28.0
delta_t=0.1
x=np.zeros(int(5/delta_t))
y=np.zeros(int(5/delta_t))
z=np.zeros(int(5/delta_t))
t=0.0
i=1
while(t<5.0):
    x[i+1]=(2*delta_t*sigma*(y[i] - x[i]))+x[i-1]
    y[i+1]=(2*delta_t*(rho*x[i] - y[i] -x[i]*z[i]))+y[i-1]
    z[i+1]=(2*delta_t*(-beta*z[i] + x[i]*y[i]))+z[i-1]
    t=t+delta_t
plt.figure()
plt.plot(x,y)
plt.savefig('xy.png')
plt.figure()
plt.plot(x,z)
plt.savefig('xz.png')