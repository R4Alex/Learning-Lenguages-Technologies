'''
This are the instructions in spanish, I'm going to add them in english after

Ejercicio 1
En este ejercicio deberás crear un script llamado personas.py que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego rocorre las personas de la lista y paracada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo previamente):


1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.

'''
from io import open

file = open('people.txt', 'r', encoding="utf8")
lines = file.readlines()
file.close()

people = []

for line in lines:
    info = line.replace("\n", '').split(";")
    person = {
        "id": info[0],
        "name": info[1],
        "lastname": info[2],
        "birthday": info[3],
    }
    people.append(person)

for person in people:
    string = "ID:{} Name: {}\nBirthday: {}\n".format(
        person['id'],
        person['name'] + " " + person['lastname'],
        person['birthday']
    )
    print(string)
