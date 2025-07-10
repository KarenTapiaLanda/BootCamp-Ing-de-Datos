def calculadora():
    while True:
        try:
            # Solicitar los números al usuario
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Solicitar el operador
            operador = input("Ingresa la operación (+, -, *, /): ")

            # Realizar la operación según el operador ingresado
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operador no válido. Usa +, -, * o /.")

            print(f"Resultado: {num1} {operador} {num2} = {resultado}")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error de división: {zde}")
        finally:
            print("Operación finalizada.\n")

        # Preguntar si desea realizar otra operación
        repetir = input("¿Deseas hacer otra operación? (s/n): ").lower()
        if repetir != "s":
            print("¡Gracias por usar la calculadora!")
            break

# Ejecutar la calculadora
calculadora()
'''
se uso un bucle while True para repetir hasta que el usuario diga que no.

try, except y finally maneja todos los errores y asegura siempre cerrar la operación.

Se Convierten las entradas a float para permitir números decimales.
'''