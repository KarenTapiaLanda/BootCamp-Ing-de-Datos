# Contadores por categoría (se acumulan durante múltiples ingresos)
contador_menores = 0
contador_adultos = 0
contador_adultos_mayores = 0

def clasificar_edad(edad):
    """
    Clasifica la edad en una categoría.
    :param edad: Edad de la persona
    :return: Cadena con la categoría correspondiente
    """
    if edad < 18:
        return "menor de edad"
    elif edad < 60:
        return "adulto"
    else:
        return "adulto mayor"

def mostrar_resumen():
    """
    Muestra un resumen general de las categorías y contadores.
    """
    print("\nRESUMEN DE CATEGORÍAS:")
    print(f"Menores de edad: {contador_menores}")
    print(f"Adultos: {contador_adultos}")
    print(f"Adultos mayores: {contador_adultos_mayores}")

# Bucle para ingresar varias personas
while True:
    nombre = input("\nIngrese su nombre: ")
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Edad inválida. Intente nuevamente.")
        continue

    categoria = clasificar_edad(edad)

    # Contabilizar según la categoría
    if categoria == "menor de edad":
        contador_menores += 1
    elif categoria == "adulto":
        contador_adultos += 1
    else:
        contador_adultos_mayores += 1

    # Mostrar mensaje personalizado
    print(f"\n Bienvenido/a {nombre}, usted es {categoria}.")

    # Preguntar si desea ver el resumen
    ver_resumen = input("¿Desea ver un resumen general de las categorías? (s/n): ").lower()
    if ver_resumen == "s":
        mostrar_resumen()

    # Preguntar si desea continuar ingresando personas
    continuar = input("\n¿Desea ingresar otra persona? (s/n): ").lower()
    if continuar != "s":
        print("\nGracias por usar el sistema. ¡Hasta luego!")
        break
