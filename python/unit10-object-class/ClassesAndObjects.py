import math
from builtins import print


class Punto:

    def __init__(self, corX = 0, corY = 0):
        self.corX = corX
        self.corY = corY
        #print('se inicializo el punto')

    def __str__(self):
        return "({},{})".format(self.corX, self.corY)

    def getCuadrante(self):
        if self.corX == 0  and self.corY == 0:
            return "Es el origen"
        elif self.corX >= 0 and self.corY >= 0:
            return "primer cuadrante"
        elif self.corX <= 0 and self.corY >= 0:
            return "Segundo cuadrante"
        elif self.corX <= 0 and self.corY <= 0:
            return "Tercer cuadrante"
        elif self.corX >= 0 and self.corY <= 0:
            return "Cuarto cuadrante"
        else:
            return "Error"

    def vector(self, po):
        a = self.corX + po.corX
        b = self.corY + po.corY
        return Punto(a, b)

    def distancia(self, po):
        x = po.corX - self.corX
        y = po.corY - self.corY
        r = (x*x) + (y*y)
        return math.sqrt(r)

'''
a = Punto(2, 3)
b = Punto(5, 5)
c = Punto(-3, -1)
d = Punto()

print(a, b, c, d)

print(a.getCuadrante())
print(c.getCuadrante())
print(d.getCuadrante())

print(a.vector(b), b.vector(a))

print(a.distancia(b), b.distancia(a))

q = a.distancia(d)
w = b.distancia(d)
e = c.distancia(d)

if q > w:
    if q > e:
        print("Q es el mas lejano")
    else:
        print("E es el mas lejano")
elif w > e:
    print("W es el mas lejano")
else:
    print("E es el mas lejano")
'''

class Rectangulo:
    def __init__(self, inicial=Punto(0, 0), final=Punto(0, 0)):
        self.inicial = inicial
        self.final = final

    def getBase(self):
        return abs(self.inicial.corX - self.final.corX)

    def getAltura(self):
        return abs(self.inicial.corY - self.final.corY)

    def getArea(self):
        return (self.getBase() * self.getAltura())/2


r = Rectangulo(Punto(2, 2), Punto(8, 6))

print(r.getArea())







