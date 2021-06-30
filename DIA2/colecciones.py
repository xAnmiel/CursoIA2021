


cad = ""
cad2 = ''


num = [1,2,3,4,5,7,6,1,9,7,3,5,1,8,4,3,6]
nombres = ["a","b", "d"]
lista = [1, "Juan", True, 1.34, [1,2,3,4]]

y =  []
x=list()
#x.append(9)

print (lista [4])
print (x)
print (y)   

print (nombres [2])
print (nombres [-1])

print (len (num))
L1=num[2:8]
print (L1)


print (num [2:8])   #El primero es inclusivo y el último exclusivo

for i in range (2,len(num)):
    print (num [i],end=' ')


num [2] = 50
del num [2]


print ("")
print (num[:])
print (num[2:])
print (num[:8])
print (num[-4:]) #Así llega al final
num.sort()
print (num)

nums = ("Yoelvis", "Francisco", 'Anmiel')

t1 = ()
t2 = tuple()
print (nums)
x=nums [1:]
print (nums)
print(type(x))

#Set
noms = {"Eduardo", 'Jesus', 'Eduardo'} #No se repiten
print (noms)

#Diccionarios

per1 = {}
per2 = dict ()

persona = {
    "nombre":"Juan",   #Valor el de la derecha
    "edad":20,          #indice el de la izquierda
    "estatura":1.63,     
}
print (persona)
print(len(persona)) #saber el tamaño
persona["nombre"] = "Maria"
persona["apellidos"] = "Rodriguez"
print (persona["nombre"])
print (persona["edad"])
print (persona.get("estatura"))

persona.pop("edad")
for e in persona:
    print(persona[e])

for e in persona.values():
    print(e)







