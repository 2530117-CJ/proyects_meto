"""

age = int(input("Escribe tu edad"))

if age >= 18:
    print("Eres mayor de edad")
else: 
    print("eres menor de edad") 
"""

"""
#try, execept
age = 0
try:
    age = int(input("Escribe tu edad "))

except:
    print("Error, ingresaste un caracter no válido")
    
if age >= 18:
        print("Eres mayor de edad")
else: 
        print("eres menor de edad")


age = -1
try:
    age = int(input("Escribe tu edad "))

except:
    print("Error, ingresaste un caracter no válido")
    
if age >= 100:
        print("Tienes mas de un siglo")

elif age >= 18 and age <100:
      print("eres mayor de edad")

elif age >= 0 and age <18:
      print("eres menor de edad")
    
else: 
        print("Tuviste un error")

"""
    
#Actividad
age = -1
try:
    age = int(input("¿Cual es tu edad? "))

except:
    print("Error, ingresaste un caracter no válido")
    
if age > 0 and age <=4 :
    print("La entrada es gratis")

elif age > 4 and age <18:
    print("La entrada cuesta 200")

elif age >=18:
    print("La entrada cuesta 400")
else: 
     print("Tuviste un error")


#Multiples if
guisos =["deshebrada", "tamales", "salsa verde", "pozole"]

if "asado" in guisos:
    print("si hay asado")

else:
    print("no hay asado")

if "deshebrada" in guisos:
    print("si hay deshebrada")

else:
    print("no hay deshebrada")

if "tamales" in guisos:
    print("si hay tamales")

else:
    print("no hay tamales")

if "pozole" in guisos:
    print("si hay pozole")

else:
    print("no hay pozole")

if "salsa verde" in guisos:
    print("si hay salsa verde")

else:
    print("no hay salsa verde")

#Utilizando variables
guisos_disponibles =["deshebrada", "tamales", "salsa verde", "pozole"]
guisos_a_ordenar =["deshebrada", "caldo de pollo", "tamales", "pozole"]

print("¿Que giso quieren ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")

    if guiso in guisos_disponibles:
        print(f"si tenemos {guiso}")
    else:
        print("no tenemos ese guiso")
