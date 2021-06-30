import numpy as np

#range (5,10,2)  el inicio, el final exclusivo y de cuanto en cuanto
a = np.arange(5,20,2)
print(a)

b = np.array([10,20,30,40],dtype=np.float16)
b = np.array([10,20,30,40],dtype='f2')

c = b.astype(np.int32)

print(b.dtype)
print(c.dtype)


d=np.ones((3,4))   #Crer matriz de 1's
print(d)

d=np.zeros((3,4))   #Crer matriz de 0's
print(d)

print("")

e=np.random.randint((3,4))
print(e)

f=np.full((5,6),5)
print(f.max())

g=np.arange(24).reshape(2,3,4)          #Arreglo tridimensional
print(g)

h=np.array([[10,11,12],[20,21,22],[30,31,32],[40,41,42]])
print(h)

cols = np.array([0,1,2,0])
rengs = np.arange(4)

#print(h[rengs,cols])
#h[rengs,cols] +=100
#print(h)

filtro = h>21
print(filtro)

i=h[filtro]
print(i)

h[h%2==0] += 100  #A todos los num pares les suma 100
print(h)

h=np.array([[10,11,12,23],[20,21,22,23],[30,31,32,23],[40,41,42,23],[40,41,42,23]])
print(h)
subh=h[:3,1:3]
print(subh)

print("")

A= np.random.randint(low=2,high=50,size=(3,3))
B= np.random.randint(low=2,high=50,size=(3,3))
print(A)
print(B)

C=np.vstack((A,B))  #Apilar verticalmente
print(C)
print ("")
C=np.hstack((A,B))   #Apila horizontal
print(C)

