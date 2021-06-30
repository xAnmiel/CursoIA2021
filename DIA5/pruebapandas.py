import pandas as pd

#Serie: Columna de una tabla        Arreglo unidimensional
#DataFrame

a=[1,5,2]

b = pd.Series(a,index=['x','y','z'])

print(b)
print(b[0])
print(b['x'])


calorias = {'Lunes':420,'Martes':300,'Miercoles':320}

c = pd.Series(calorias,index=['Lunes','Miercoles'])

print(c)
print(c[0])
print(c['Lunes'])

#DataFrame                      Arreglo dimensional

datos = {
    'calorias':[420,300,320],
    'Duración':[50,40,45]
}

d=pd.DataFrame(datos,index=['Lunes','Martes','Miercoles'])
print(d)
print(d.loc[['Lunes','Miercoles']])

#datos.xlsx
