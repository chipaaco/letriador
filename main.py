# --- MÓDULOS Y PAQUETES ---

# -- Librería estándar

import os # usado para limpiar terminal
# import time: nos puede servir para hacer un timer después




# --- VARIABLES GLOBALES ---
letra = []
estatus = 0




# --- Funciones Utilitarias ---

# Limpiar la terminal de cualquier sistema operativo
def limpiar():
    if os.name == 'nt':
        os.system('cls') # si el sistema es windows
    else:
        os.system('clear') # si el sistema se parece a UNIX (linux o mac)

def mostrar_estatus():
    texto = "Estatus: "
    if estatus == 0:
        print(texto + "la letra todavia no se carga")
    elif estatus == 1:
        print(texto + "La letra está cargada")
    elif estatus == 2:
        print(texto + "Archivo LRC Generado")
    else:
        print("algo mal con la variable estatus " + estatus)




# --- Funciones #1: generar letra del programa ---

def formatear_letra(letra_descuageringada):
    lista_arreglada = []
    for verso in letra_descuageringada:
        if verso != "":
            lista_arreglada.append(verso)

    return lista_arreglada

def cargar_letra():
    print("crear una lista")
    print("Pegá o escribí acá el contenido de la letra que hayas encontrado en internet y luego apretá Ctrl-D o Ctrl-Z para guardarlo.")
    print("")

    while True:
        try: # pide al usuario que ingrese texto infinitamente
            verso = input()
        except EOFError: # cambia la acción que ocurre por defecto cuando se presiona Ctrl + c o Ctrl + c por un break que corta el ciclo infinito
            break
        global letra
        letra.append(verso) # agrega al final de la lista, cada línea (verso) que va ingresando el usuario

    print("")
    print("Esta es la lista que se generó:")
    letra = formatear_letra(letra)
    print(letra)
    print("")
    print("¿Estás satisfecho/a?")
    satisfaccion = input("Presioná cualquier tecla para continuar, o (r) para volver a cargar: ")
    if satisfaccion == "r":
        letra = []
        input("Entendido, volvamos a cargar la letra")
        limpiar()
        cargar_letra()

    else:
        global estatus # para modificar la variable que esta afuera de la función
        estatus = 2
        input("Perfecto, ahora podés continuar con la opción 2")




# --- Funciones #2: generar archivo .lrc ---

def generar_lrc():
    if estatus != 2:
        print("No se puede generar nada si no se carga una letra primero")
        input()
    else:
        print("Vas a generar tu archivo .lrc")
        print("Tené a mano un reproductor con tu canción, y la empieces a reproducir presioná enter en este programa")
        print("Cada vez que se escuche entonar la estrofa que aparece por pantalla, precioná (enter)")
        print("Si te equivocaste, y querés reiniciar la generación del archivo, precioná (r) seguido de enter")
        print("Cuando la canción termine de reproducirse precioná (t) seguido de enter")
        print("Cuando la cancion termine presiona (q)")
        print("")
        accion = 0
        while accion != "q":
            accion = input("Acción elegida: ")
            if accion == "":
                print("mostrar linea agregada al archivo .lrc [00:00:00] verso que se esta cantando")
                accion = 0
            elif accion == "r":
                print("ok, todos nos equivocamos, empecemos de cero...")
                # poner una confirmacion: seguro? si o no
                accion = 0




# --- FUNCIÓN PRINCIPAL ---

def main():
    limpiar()
    print(" _      _        _           _")
    print("| | ___| |_ _ __(_) __ _  __| | ___  _ __")
    print("| |/ _ \ __| '__| |/ _` |/ _` |/ _ \| '__|")
    print("| |  __/ |_| |  | | (_| | (_| | (_) | |")
    print("|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|")
    print("")
    mostrar_estatus()
    print("")
    print("Opciones:")
    print("1: cargar letra al programa")
    print("2: generar archivo lrc")
    print("3: ayuda")
    print("4: salir")
    print("")

    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiar()
        cargar_letra() # crea una lista, sus elementos son los versos de la letra proveída por el usuario
        main()

    elif opcion == '2':
        limpiar()
        generar_lrc()
        # le pide al usuario el nombre del archivo de la cancion .mp3, flac, etc para crear el archivo.mp3.lrc que se creara
        # le avisa al usuario que debe reproducir la cancion en segundo plano
        # mientras no se presione Q, el generador no se detiene
        #   el usario debe avisar con Enter cuando empieza el contador
        #       el programa marca el momento en que arranca la cancion en el archivo de salida
        #   cada que se presione Enter el programa agrega el momento del contador en que se presiono y concatena el verso correspondiente a su lado, el contador incrementa para seleccionar el siguiente elemento, y asi hasta que se corte el bucle
        #   en caso que el usuario presione R, el generador se reiniciará.
        # una vez fuera del bucle, se le preguntara al usuario si quiere visualizar el contenido del archivo, y se mostrara la ubicacion del archivo generado, y se sugerira que el usuario corte lo ubique manualmente en la misma ruta que su archivo de musica original.
        main()

    elif opcion == '3':
        print("")
        print("¿Que es un archivo lrc?")
        print("")
        print("Es un archivo que comparte la misma ruta y nombre que un archivo de audio (mp3, flac, wav, etc), contiene el momento exacto en que se canta una estrofa en una canción. Una característica es que su archivo termina con la extensión .lrc.")
        print("")
        input("Precioná cualquier tecla para volver al inicio: ")
        main()
    elif opcion == '4':
        print("¡Gracias por usar!")
    else:
        input("Opción no válida. Apretá Enter para continuar...")
        main()

if __name__ == "__main__":
    main()

