# main.py

import operaciones

def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    print(f"Suma: {operaciones.sumar(a, b)}")
    print(f"Resta: {operaciones.restar(a, b)}")
    print(f"Multiplicación: {operaciones.multiplicar(a, b)}")

    try:
        print(f"División: {operaciones.dividir(a, b)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
