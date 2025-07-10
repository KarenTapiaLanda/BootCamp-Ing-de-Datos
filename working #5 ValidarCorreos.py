import re  # Necesario para la validación de correos electrónicos

class Persona:
    def __init__(self, nombre, edad, correo_electronico):
        self.nombre = nombre
        self.edad = edad
        self.correo_electronico = correo_electronico

    # Mostrar datos de la persona en un formato amigable
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.correo_electronico}")

    # Validar si el correo electrónico tiene un formato válido
    def validar_correo(self):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, self.correo_electronico))

    # Actualizar los datos de la persona (de forma opcional)
    def actualizar_datos(self, nombre=None, edad=None, correo_electronico=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if correo_electronico:
            self.correo_electronico = correo_electronico

    # Verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Función adicional: Comparar edades entre dos personas
def comparar_edades(persona1, persona2):
    if persona1.edad > persona2.edad:
        return f"{persona1.nombre} es mayor que {persona2.nombre}"
    elif persona1.edad < persona2.edad:
        return f"{persona2.nombre} es mayor que {persona1.nombre}"
    else:
        return f"{persona1.nombre} y {persona2.nombre} tienen la misma edad"
# Crear dos personas
p1 = Persona("Ana", 25, "ana@mail.com")
p2 = Persona("Luis", 30, "luis123@email.com")

# Mostrar datos
p1.mostrar_datos()
p2.mostrar_datos()

# Validar correos
print("Correo de Ana válido:", p1.validar_correo())
print("Correo de Luis válido:", p2.validar_correo())

# Verificar mayoría de edad
print("Ana es mayor de edad:", p1.es_mayor_de_edad())
print("Luis es mayor de edad:", p2.es_mayor_de_edad())

# Comparar edades
print(comparar_edades(p1, p2))

# Actualizar datos de Ana
p1.actualizar_datos(edad=35, correo_electronico="ana.nueva@mail.com")
p1.mostrar_datos()
