# Capturar datos desde la consola
nombre = input("Ingrese su nombre: ")
edad_input = input("Ingrese su edad: ")
pais_input = input("Ingrese su país de residencia: ")

# Conversión de edad y país para validación
edad = int(edad_input)
pais = pais_input.lower()

# Verificar si cumple las condiciones para el beneficio
paises_validos = ["argentina", "chile", "colombia"]
acceso_beneficio = edad >= 18 and pais in paises_validos

# Mostrar mensaje personalizado
print(f"\nHola {nombre}, tienes {edad} años y vives en {pais_input.title()}.")

if acceso_beneficio:
    print("Puedes acceder al beneficio.")
else:
    print("No puedes acceder al beneficio. Debes tener al menos 18 años y vivir en Argentina, Chile o Colombia.")
