#def suma (x,y):
 #   return x+y

def resta (x=20,y=10):    
    return x-y

def suma2(*args):   #El asterisco representa que recibe muchos valores #Lo va a guardar en la variable como tupla
    total=0
    for valor in args:
        total+=valor      
    return total 

def personas(**kwargs):               #kwargs
    print (kwargs)

def combinacion(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

def mensaje(nombre):
    print ("Hola, ",nombre," bienvenido al curso de IA")
    print ("Hola {1} {0}, bienvenido".format(nombre,0))
    print ("Hola {0} {1}, bienvenido".format(nombre,0))


#Función que regrese varios valores
def obtener_datos():
    return "juan2", 15,1.67

def crear_persona():
    return {'nombre':'Juan','edad':15,'estatura':1.67}


#Funciones Lambdas
def suma (x,y):
    return x+y
suma=lambda x,y:x+y
