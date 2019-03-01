

'''

1) Formatea los siguientes valores para mostrar el resultado indicado:

"Hola Mundo" → Alineado a la derecha en 20 caracteres
"Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
"Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
150 → Formateo a 5 números enteros rellenados con ceros
7887 → Formateo a 7 números enteros rellenados con espacios
20.02 → Formateo a 3 números enteros y 3 números decimales




# Completa el ejercicio aquí
print( "{:>20}".format("Hola Mundo") )
print( "{:.3}".format("Hola Mundo") )
print( "{:^20.1}".format("Hola Mundo") )
print( "{:05d}".format(150) )
print( "{:7d}".format(7887) )
print( "{:7.3f}".format(20.02) )

'''



'''

2) Crea un script llamado tabla.py que realice las siguientes tareas:

Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
El script contendrá un bucle for que itere el número de veces del primer argumento.
Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
Ejecuta el código y observa el resultado.
Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.

Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo sys y su lista argv:

import sys
print(sys.argv) # argumentos enviados

'''

import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')





















