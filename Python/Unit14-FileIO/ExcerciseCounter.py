'''
This are the instructions in spanish, I'm going to add them in english after

Ejercicio 2
En este ejercicio deberás crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt que almacenará un contador de visitas (será un número):

Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
Luego a partir de un argumento:
Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.

'''

from io import open
import sys

file = open('counter.txt', 'a+')
file.seek(0)
data = file.readline()
file.close()

if data == '':
    count = 0
else:
    try:
        count = int(data)
    except:
        print("File corrupted")

if sys.argv[1] == "inc":
    count += 1
    print("Value has increased {}".format(count))
elif sys.argv[1] == 'dec':
    count -= 1
    print("Value has decreased {}".format(count))
else:
    print("Count Value is: {}".format(count))

file = open('counter.txt', 'w')
file.write(str(count))

