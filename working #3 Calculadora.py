def calculadora():
    try:
        # Paso 2: Solicitar números y operador
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        operador = input("Ingresa el operador (+, -, *, /): ")

        # Paso 3: Realizar operación según el operador
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            if numero2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = numero1 / numero2
        else:
            raise ValueError(f"Operador inválido: {operador}")

        print(f"Resultado: {numero1} {operador} {numero2} = {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error matemático: {zde}")
    finally:
        print("Operación finalizada.")

# Llamar a la función para ejecutar la calculadora
calculadora()
