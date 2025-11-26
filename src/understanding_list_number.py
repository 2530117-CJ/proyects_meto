"""
    Las listas tambien pueden almacenar numeros
    y de echo, son ideales para esto.
    Python ofrece una gran cantidad de herramientas 
    que ayudan a trabajar eficientemente listas de numero
"""

#Metodo built_in range ()
"""
    El metodo range() nos ayuda a crear facilmente serie de numeros
    ejemplo:
"""
for value in range(10): # 10 nuemeros del 0 al 9 
    print(value)

print("Numeros del 0 al 9")
for value in range(1, 10): # 10 nuemeros del 0 al 9 
    print(value) 

print("Numeros impares del 1 al 9")
for value in range(1, 10, 2): # 10 nuemeros impares del 0 al 9 
    print(value)
odd_numbers = list(range (1, 10, 2)) 
print(odd_numbers)

print("Numeros pares del 1 al 9")
for value in range(0, 10, 2): # 10 nuemeros pares del 0 al 9 
    print(value)
par_numbers = list(range (0, 10, 2)) 
print(par_numbers)

print("tabla del 9")
for value in range(0, 91, 9): # 10 nuemeros pares del 0 al 9 
    print(value)
tabla_nueve_numbers = list(range (0, 91, 9)) 
print(tabla_nueve_numbers)


#Cuadrados de los primeros 10 numeros
squeres = []

for number in range(1, 11):
    squere = number** 2
    squeres.append(squere)
print(squere)

##as metodos built min ()