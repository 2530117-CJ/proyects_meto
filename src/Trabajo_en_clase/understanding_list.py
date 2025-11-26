#lists
"""
    Las listas son elementos mutables

    Las listas nos prmiten almacenar informacion en un lugar,
    la cantidad que tengas: ya sean pocos elementos o millones 
    de elementos

    Se recomienda nombrar una variable del tipo lista en plurar.
    En python los corchetes[] definen una lista, cus elementos 
    van separados por comas.
    Por ejemplo: 
"""
bicycles = [ "trek", "canondale", "redline", "specialized", "giant"]
print(bicycles)

print(bicycles[0].title())

# Los indices comienzan en cero y terminan en n-1, donde n es el numero de elementos
print(bicycles[4].title())

#Accediendo al ultimo elemento
print(bicycles[-1].title()) #Este seria el ultimo
print(bicycles[-2].title())
print(bicycles[-5].title()) #Este seria el ultimo

#Utlizando valores de la lista.
message = "Mi primera bicicleta fue una " + bicycles[4].title() +"."
print(message)

message_f = f"Mi primera bicicleta fue una {bicycles[4].upper()}."
print(message_f)

message_f = f"Mi primera bicicleta fue una {bicycles[4].capitalize()}." #Solo convierte la primera letra de un texto
print(message_f)

##Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)
print("metodo de las listas para agregar elementos; list_name.append(element)")
bicycles.append("ducatti")
print(bicycles)

#Metodo append
print("\n ---Agregar elementos a una lista metodo append() ---")
motorcycles = ["Honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append ("ducati")
print(motorcycles)

"""
Agrgar elementos a una lista en una posicion especifica
    -insert (): Inserta un elemento en una pocision especifica 
"""

print("\n ---Agrgar elementos a una lista metodo insert ()---")
motorcycles = ["Honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert (1, "ducati")
print(motorcycles)

"""
Eliminar elementos de una lista 
    -del(): Elimina un elemento en una pocision especifica 
"""

print("\n ---Eliminar elementos a una lista metodo del ()---")
motorcycles = ["Honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles [0]
print(motorcycles)

"""
Eliminar elementos de una lista y utilizar el valor inmediato
    -pop(): Elimina y devuelve el ultimo elemento de la lista
"""

print("\n ---Eliminar y delvover elementos a una lista metodo pop()---")
motorcycles = ["Honda", "yamaha", "suzuki"]
print(motorcycles)
last_motorcycles = motorcycles.pop()
print(last_motorcycles)
print (f"la motocicleta que eliminaste fue {last_motorcycles}")

print("\n ---Eliminar y delvover elementos a una lista metodo pop()---")
motorcycles = ["Honda", "yamaha", "suzuki"]
print(motorcycles)
last_motorcycles = motorcycles.pop(1)
print(last_motorcycles)
print (f"la motocicleta que eliminaste fue {last_motorcycles}")

"""
Eliminar elementos de una lista y utilizar el valor inmediato
    -remove(): Elimina La priera aparicion de un valor especifico de la lista
"""

print("\n ---Eliminar y delvover elementos a una lista metodo remove()---")
motorcycles = ["Honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print (motorcycles)
print("\n")

"""
Organizar listas de manera permanentemente
    -sort(): Ordena la lista de manera alfabeticamente
"""

print("\n ---Organizar listas de manera permanentemente metodo sort()---")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.sort()
print (motorcycles)
print("\n")


"""
Ejemplo
"""
students = ["jesus", "joshue", "andrik", "jen", "miguel", "africa"]
print(students)
desaired_students = input("¿ue estudiante quieres eliminar?")
students.remove(desaired_students.strip().lower())
print (students)
students.reverse ()
print (students)

print (len(students))

cars =["kia", "ford", "tesla", "volvo", "chevy"]
print (sorted(cars))
sorted_list = sorted (cars)
print ("lista original", cars)