"""
Un string es de manera sencilla una serie de caracteres.
En python todo lo que se encuentre dentro de comillas simples (´´) o dobles (" ")
sera considerado un string

"""

name = "clase de programación"
print(name)

#title 
print(name.title()) 
"""
    Un metodo es una accion que python puede realizar 
en un fragmento de datos o sobre una variable

    El punto despues de una variable seguido del metodo title () dice que
se tiene que ejecutar el metodo title() de la variable name

    Todos los metodos van seguidos de parentesis porque 
en ocasiones necesitan informacion adiccional
para funcionar, la cual iria dentro del parentesis. 
En esta ocasion, el metodo .title() no requiere informacon
adicional para funcionar
"""
print("metodo upper", name.upper())
print("metodo lower", name.lower())

# Concatenacion de STRINGS
first_name = "Cecya"
last_name = "jimenez juarez"
full_name = first_name + " " + last_name

print(full_name)
print(full_name.title())

#Whitespece
"""
Un whitespece se refiere a cualquier caracter que no se imprime,
es decir, un espacio, tabuador, y finales de lineas. Tambien se utilizan 
comunmente para organizar las salidas de tal manera que sea mas amigable 
de leer o ver para el usuario

Ejemplo:
 -tabulador: \t
 -salto de linea: \n

"""

print("Whitespace Tabulador")
print("phyton")
print("\tPhton")
print("\t\tpython")

print("Whitespace salto de linea")
print("languagues: \npython \n C \nJavaScript")

#Eliminación de espacios en blanco
programing_languages = " Python "

print(programing_languages)
print(programing_languages.rsplit())
print(programing_languages.lstrip())
print(programing_languages.strip())

#Syntax Error con Strings
""""
menssage = "Una fortaleza de python es su comunidad"
menssage = "Una fortaleza "de python" es su comunidad" - Error de syntax

"""