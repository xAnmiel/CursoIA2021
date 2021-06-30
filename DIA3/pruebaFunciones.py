import funciones as f
from funciones import suma

print(suma(400,5))


x,y,z=f.obtener_datos()
print(x,y,z)
print("")

#p=crear_persona()
print(f.crear_persona()['nombre'])
print("")

#r=suma (4,5)
print(f.suma(4,5))
f.mensaje("Juan")


print(f.resta(40,5))
print(f.suma2(1,5,8,9,20))

print("")

f.personas(nombre="juan",edad=15)

f.combinacion('manzana',10,20,30,nombre='juan',edad=15)
