class Asiento:
    def __init__(self, color="negro"):
        self.color = color

    def cambiarColor(self, color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color.lower() in colores_permitidos:
            self.color = color.lower()

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo.lower() in ["electrico", "gasolina"]:
            self.tipo = tipo.lower()

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, marca, registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.registro = registro
        self.asientos = []
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        registros = [self.registro] + [asiento.registro for asiento in self.asientos]
        registros += [self.motor.registro]
        if len(set(registros)) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"
