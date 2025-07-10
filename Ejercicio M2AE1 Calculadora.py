# Función para suma
def sumar(a, b):
    return a + b

# Función para resta
def restar(a, b):
    return a - b

# Función para multiplicación
def multiplicar(a, b):
    return a * b

# Función para división
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b

# Función principal
def calculadora():
    while True:
        print("\nOperaciones disponibles: suma, resta, multiplicacion, division")
        operacion = input("¿Qué operación deseas realizar? (o escribe 'salir' para terminar): ").lower()

        if operacion == "salir":
            print("¡Gracias por usar la calculadora!")
            break

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if operacion == "suma":
                resultado = sumar(num1, num2)
            elif operacion == "resta":
                resultado = restar(num1, num2)
            elif operacion == "multiplicacion":
                resultado = multiplicar(num1, num2)
            elif operacion == "division":
                resultado = dividir(num1, num2)
            else:
                print("Operación no reconocida. Intenta con suma, resta, multiplicacion o division.")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números.")
        except ZeroDivisionError as zde:
            print(zde)

# Ejecutar la función principal
calculadora()
