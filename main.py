from calculadora import *
from operaciones import *

def main():
    while True:
        opcion = menu()
        if opcion == 0:
            print("Saliendo de la calculadora...")
            break
        elif opcion == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {suma(a, b)}")
        elif opcion == 2:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {resta(a, b)}")
        elif opcion == 3:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == 4:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            try:
                print(f"Resultado: {division(a, b)}")
            except ValueError as e:
                print(e)
        elif opcion == 5:
            a = float(input("Ingrese la base: "))
            b = float(input("Ingrese el exponente: "))
            print(f"Resultado: {potencia(a, b)}")
        elif opcion == 6:
            a = float(input("Ingrese un número: "))
            try:
                print(f"Resultado: {raiz(a)}")
            except ValueError as e:
                print(e)
        elif opcion == 7:
            n = int(input("Ingrese un número entero no negativo: "))
            try:
                print(f"Resultado: {factorial(n)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida. Intente de nuevo.")

main()