class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Carro(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


# Completa el ejercicio aquí

class Camioneta(Carro):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

'''
def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(type(vehiculo).__name__, vehiculo)
'''

'''Se tiene que utilizar un solo metodo, '''

def catalogar(vehiculos, ruedas):
    for vehiculo in vehiculos:
        if vehiculo.ruedas == ruedas:
            print(type(vehiculo).__name__, vehiculo)


vehiculos = []

vehiculos.append(Vehiculo("rojo", 2))
vehiculos.append(Carro("azul", 3, 200, 4))
vehiculos.append(Camioneta("verde", 4, 250, 6, 15))
vehiculos.append(Bicicleta("rojo", 2, "montaña"))
vehiculos.append(Motocicleta("Violeta", 2, "urbana", 300, 4))

catalogar(vehiculos)












