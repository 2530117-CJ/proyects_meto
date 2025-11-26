#tuplas
"""
Las tuplas son las listas de elementos que no cambian
de tamaño. Las tuplas son INMUTABLES. Se utilizan los ()
para definir una tuplas, Los [] son para las listas 
"""

rectangle_measures = (200, 50) #largo , ancho
print(rectangle_measures[0])
print(rectangle_measures[1])

for measure in rectangle_measures:
    print(measure)

print(dir(rectangle_measures))#Es para saber que metodos tiene

#Reglesando a las listas tantito
cars =["bwm", "porche", "masda"]
cars[0]="bwm"
cars[1]="porshe"
cars[2]="mazda"
print(cars)

#Para cambiar el valor en la tupla
rectangle_measures = (200, 50) #largo , ancho
rectangle_measures = (300, 100) #largo , ancho
rectangle_measures = (300, 100, 50) #largo , ancho

"""
No podemos modificar una tupla directamente lo que si podemos hacer es cambiar
la asignacion a una variable que almacena una tupla.
"""