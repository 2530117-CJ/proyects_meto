while True :
    try :
        number = int(input("ingrese un numero entre 10 y 20 "))
        if 10 <= number <= 20 :
            print("gracias por ingresar un numero valido")
            break
        else :
            print("numero invalido, intente de nuevo")
    except ValueError :
        print("entrada invalida, por favor ingrese un numero entero")   
    except KeyboardInterrupt :
        print("\nOperacion cancelada por el usuario")
        break

print("Programa terminado")
        