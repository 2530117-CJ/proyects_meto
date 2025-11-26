# Trabajando con listas 
"""
    Recorer una lista sin importar la cantidad
    de elementos que tenga
"""

magicians = ["ron", "hermione", "harry"]

for magician in magicians:
    print (magician)
    print (magician.upper())
    print (f"{magician.title()} ese fue un gran hecizo")
    print (f"{magician.lower()} No podemos esperar para ver tu siguiente hechizo")
    print ("\n")  

print("Gracias a todos, fue un gran espectaculo")

"""
Identacion_
    Python utiliza la identacion para determinar
    cuando una linea de codigo esta conectada a 
    la linea de codigo anterior

    Basicamente, se utilizan 4 espacios en blancos
    para obligarnos a escribir codigo ordenado y
    estructurado
"""

# No olvidemos identitar
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print (magician)
print(f"I can´t wait to see your next trick, {magician.title()}")

# Identacion inecesaria
message = "Hola python"
print(message)