"""
squares=[]
for value in range (0,11):
    square = value**2
    squares.append(square)
print(squares)
"""

"""
Una list comprehention cambina el ciclo for y la cracion 
de unos elementos en una sola linea y automaticamente 
agregar ucada nuevo elemento a la lista, es decir, sin 
utlizar el metodo append
"""

squares = [value**2 for value in range(0, 11)]

#para generar los numeros prares entre el 0 y el 100
evens_ranges = [value**2 for value in range(0,101, 11)]

evens_if = [value for value in range(0,101) if value%2==0]
impar_if = [value for value in range(0,101) if value%2==1]
print(evens_if,"\n\n" ,impar_if)
