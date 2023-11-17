def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    
    cantidad_de_letras_de_palabra_a_encontrar = 5

    letras_verificadas = []

    #Iteramos por cada letra de la palabra ingresada
    for posicion in range(cantidad_de_letras_de_palabra_a_encontrar):

        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]   

        
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:

            letras_verificadas.append("[" + palabra_ingresada[posicion] + "]")

        
        elif la_letra_existe_en_la_palabra:

            letras_verificadas.append("(" + palabra_ingresada[posicion] + ")")
        
        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    
    return letras_verificadas

    
def imprimir_grilla():

    for palabra in lista:
        print (palabra)

        #Crear nuestro juego

palabra_a_encontrar = "arbol"
intentos = 5
cantidad_de_letras = 5

grilla = []

print('Bienvenidos al juego')

while intentos > 0:
    print("Te quedan", intentos, "intentos")
    palabra_ingresada = input("Ingrese una palabra: ")
    intentos = intentos - 1

    if (len(palabra_ingresada)) != cantidad_de_letras:
        print("La palabra ingresada no tiene la cantidad de letras correctas")
        print("Ingresar una palabra con", cantidad_de_letras, "letras")
        continue
    else:
        linea_verificada = obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)

    if palabra_ingresada == palabra_a_encontrar:
        print("Felicidades, ganaste 📣​")
        break
    
print("Te quedaste sin intentos")