'''
# Completa el ejercicio aquí# Compl
textoOriginal = "un día que el viento soplaba con fuerza#mira como se " \
        "mueve aquella banderola -dijo un monje#lo que se mueve es " \
        "el viento -respondió otro monje#ni las banderolas ni el viento, " \
        "lo que se mueve son vuestras mentes -dijo el maestro"

splittedText = textoOriginal.split("#")

for i, text in enumerate(splittedText):
    if i == 0:
        print(text.capitalize(), "...")
    print("- " + text + ".")

'''

'''
Finalmente, después de ejecutar la función, comprueba que la 
suma de todos los números a partir del segundo, concuerda 
con el primer número de la lista, tal que así:
'''

def modificar(lista):
    nuevaLista = lista.copy()
    #Quitarle duplicados
    nuevaLista = set(nuevaLista)
    nuevaLista = list(nuevaLista)
    nuevaLista.sort()
    nuevaLista.reverse()

    for elemento in nuevaLista:
        if elemento % 2 != 0:
            nuevaLista.remove(elemento)

    nuevaLista.insert(0, sum(nuevaLista))

    return nuevaLista


# Completa el ejercicio aquí
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

nuevaLista = modificar(lista)

print(nuevaLista)
print( nuevaLista[0] == sum(nuevaLista[1:]))










