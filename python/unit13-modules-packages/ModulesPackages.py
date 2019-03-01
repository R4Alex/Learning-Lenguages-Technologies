#Seccion incompleta

'''
from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

print("{} + {} = {}".format(a, b, suma(a, b)))
print("{} - {} = {}".format(b, d, resta(b, d)))
print("{} * {} = {}".format(b, b, producto(b, b)))
print("{} / {} = {}".format(a, c, division(a, c)))

'''

'''
import datetime
import os
import time

while(True):
    os.system("cls")
    dtObject = datetime.datetime.now()
    print("{}:{}:{}".format(dtObject.hour, dtObject.minute, dtObject.second))
    time.sleep(1)
    
'''

'''
**3) Crea un script llamado generador.py que cumpla las siguientes necesidades:**

* Debe incluir una función llamada **leer_numero()**. Esta función tomará 3 valores:
 **ini**, **fin** y **mensaje**. El objetivo es leer por pantalla un número >= que 
 ini y <= que fin. Además a la hora de hacer la lectura se mostrará en el input el 
 **mensaje** enviado a la función. Finalmente se devolverá el valor. Esta función 
 tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo 
 escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).
'''

import random
import math


def leerNumero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error: Numero no valido")
        else:
            if valor >= ini and valor <= fin:
                break

    return valor


def generador():
    numeros = leerNumero(1,20, 'Cuantos numeros quieres generar: ')
    modo = leerNumero(1, 3, '¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ')

    lista = []
    for i in range(numeros):
        value = random.uniform(1, 100)
        print(value, '\t', end="")
        if modo == 1:
            r = math.ceil(value)
            print(r)
            lista.append(r)
        elif modo == 2:
            r = math.floor(value)
            print(r)
            lista.append(r)
        elif modo == 3:
            r = round(value)
            print(r)
            lista.append(r)
    return lista


print(generador())


















