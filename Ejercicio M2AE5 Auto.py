class Auto:
    def __init__(self, color, peso, tamaño, alto, largo, ruedas, puertas, tipo):
        self.color = color
        self.peso = peso
        self.tamaño = tamaño
        self.alto = alto
        self.largo = largo
        self.cantidad_ruedas = ruedas
        self.cantidad_puertas = puertas
        self.tipo = tipo

        self.estado = "detenido"  # Estado inicial del auto

    # Mostrar información del auto
    def mostrar_info(self):
        print(f"Auto tipo: {self.tipo}, Color: {self.color}, Estado: {self.estado}")
        print(f"Dimensiones (alto x largo): {self.alto} x {self.largo}")
        print(f"Peso: {self.peso} kg, Tamaño: {self.tamaño}")
        print(f"Ruedas: {self.cantidad_ruedas}, Puertas: {self.cantidad_puertas}")

    # Comportamientos:
    def arrancar(self):
        if self.estado == "detenido":
            self.estado = "circulando"
            print("El auto ha arrancado y ahora está circulando.")
        elif self.estado == "circulando":
            print("El auto ya está en movimiento.")
        elif self.estado == "dañado":
            print("No se puede arrancar, el auto está dañado.")
        else:
            print("Acción no permitida desde el estado actual:", self.estado)

    def frenar(self):
        if self.estado == "circulando":
            self.estado = "detenido"
            print("El auto ha frenado y ahora está detenido.")
        else:
            print("No se puede frenar si no está circulando.")

    def acelerar(self):
        if self.estado == "circulando":
            print("El auto acelera.")
        elif self.estado == "detenido":
            print("Primero debes arrancar el auto.")
        elif self.estado == "dañado":
            print("No puedes acelerar, el auto está dañado.")
        else:
            print("Acción no válida en este estado.")

    def girar(self, direccion):
        if self.estado == "circulando":
            print(f"El auto gira hacia la {direccion}.")
        else:
            print("Solo puedes girar si el auto está circulando.")

    def estacionar(self):
        if self.estado in ["detenido", "circulando"]:
            self.estado = "estacionado"
            print("El auto ha sido estacionado.")
        else:
            print("No puedes estacionar en este estado.")

    def chocar(self):
        self.estado = "dañado"
        print("El auto ha sufrido un accidente y está dañado.")
# Crear autos diferentes
auto1 = Auto("Rojo", 1200, "mediano", 1.5, 4.0, 4, 4, "sedán")
auto2 = Auto("Azul", 1500, "grande", 1.8, 4.5, 4, 5, "SUV")

# Probar comportamientos de auto1
print("AUTO 1")
auto1.mostrar_info()
auto1.arrancar()
auto1.acelerar()
auto1.girar("izquierda")
auto1.frenar()
auto1.estacionar()
auto1.chocar()
auto1.arrancar()  # No debería arrancar

print("\nAUTO 2")
auto2.mostrar_info()
auto2.arrancar()
auto2.girar("derecha")
auto2.acelerar()
