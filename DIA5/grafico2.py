import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,3,4,5,6,7,9])
y = np.array([4,7,2,4,7,8,3])

x1 = np.array([1,3,4,5,6,7,9])
y2 = np.array([6,9,4,7,8,9,8])

#plt.plot(x,linestyle='dotted')
#plt.bar(x,y,label='barra',color='b')
#plt.plot(x,y,x1,y2)

"""
plt.plot(y)
plt.plot(y2)


plt.title('Edades vs estaturas')
plt.xlabel('edades')
plt.ylabel('estaturas')
#plt.grid()                      #Para ver con rejillas
plt.grid(axis='x')              #Solo rayas en el eje de las x
"""
"""""
plt.subplot(1,2,1)
plt.plot(y)
plt.subplot(1,2,2)
plt.plot(y2)                                    #separar graficos    horizontal
"""""

plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(y2)                                    #separar graficos    vertical

plt.show()



