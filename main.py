# --- MÓDULOS Y PAQUETES ---

# -- Librería estándar

# import time: nos puede servir para hacer un timer después

# -- Del proyecto

from utilidades import limpiar # para limpiar la terminal
from cargar_letra import main as cargar_letra
from generador import main as generar_lrc




# --- FUNCIÓN PRINCIPAL ---

def main():
    limpiar()
    print(" _      _        _           _")
    print("| | ___| |_ _ __(_) __ _  __| | ___  _ __")
    print("| |/ _ \ __| '__| |/ _` |/ _` |/ _ \| '__|")
    print("| |  __/ |_| |  | | (_| | (_| | (_) | |")
    print("|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|")
    print("")
    print("Estatus: la letra todavia no se carga")
    print("")
    print("Opciones:")
    print("1: cargar letra al programa")
    print("2: generar archivo lrc") # deberia de haber una comprobacion, de que si la letra no fue cargada no deje generar el archivo
    print("3: ayuda")
    print("4: salir")
    print("")
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiar()
        cargar_letra() # crea una lista, sus elementos son los versos de la letra preveida por el usuario
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

