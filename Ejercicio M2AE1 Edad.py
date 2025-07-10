# Función que verifica si la persona es mayor de edad
def es_mayor(edad):
    return edad >= 18

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
try:
    edad = int(input("Ingrese su edad: "))

    # Verificar si es mayor o menor de edad
    if es_mayor(edad):
        print(f"Hola {nombre}, eres mayor de edad con {edad} años.")
    else:
        print(f" Hola {nombre}, eres menor de edad con {edad} años.")

except ValueError:
    print("Error: Debes ingresar un número válido para la edad.")
