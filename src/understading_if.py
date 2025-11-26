cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    print(car)
    if car == "bmw" or car =="tesla" : #Los dos iguales son una comparicion y es obligatorio 
        print(car.upper())

    else:
        print (car)    

# Condicionales es el corazón del if
#Condicional verdadero
car = "bmw"
print(car == "bmw")

#condicional false a true
car_2 = "audi"
print(car_2.lower() =="Audi")

#condicional false
car_2 = "audi"
print(car_2 =="Audi")

#Condicianal = para determinar desigualdad
requesting_toping ="mushrooms"
if requesting_toping != "anchovies":
    print("Hold the anchovies")

#Comparacion numericas
age = 18 
print(age ==18)

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta vuelve a intentarlo")

age = 19
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)