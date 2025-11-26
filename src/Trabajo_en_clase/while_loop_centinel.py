"""
Docstring for understading_while_loop_centinel.
    Un programa que
        -cuente cuantos nmeros ingresa el usuario
        -Ralize la suma de los nmeros ingresados
        -Me diga cual es el maximo de los numeros ingresados
        -Me diga cual es el minimo de los numeros ingresados
"""
counter = 0
sum_numbers = 0.0
min_number = None
max_number = None

while True:
    print("Para terminar el programa ingrese 'exit'")
    user_inpput = input("Ingresa una cantidad (MXN):")

    if user_inpput == 'exit':
        break

    try:
        value = float(user_inpput)
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero valido o 'exit' para terminar.")
        continue

    except KeyboardInterrupt:
        print("\nOperacion cancelada por el usuario")
        break
    counter += 1
    sum_numbers += value

    if min_number is None or value < min_number:
        min_number = value
    if max_number is None or value > max_number:
        max_number = value
    
print(f"Cantidad de numeros ingresados: {counter}")
print(f"Suma de los numeros ingresados: {sum_numbers}")
print(f"Numero minimo ingresado: {min_number}")
print(f"Numero maximo ingresado: {max_number}")
    