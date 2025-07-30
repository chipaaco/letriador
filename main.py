import os

def main():
    os.system("clear")
    print(" _      _        _           _")
    print("| | ___| |_ _ __(_) __ _  __| | ___  _ __")
    print("| |/ _ \ __| '__| |/ _` |/ _` |/ _ \| '__|")
    print("| |  __/ |_| |  | | (_| | (_| | (_) | |")
    print("|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|")
    print("")
    print("Opciones:")
    print("1: cargar letra desde archivo")
    print("2: generar archivo lrc")
    print("3: ayuda")
    print("4: salir")
    print("")
    opcion = input("Elija una opción: ")
    if opcion == '1':
        # cargar_archivo()
        #   leer_de_ruta()
        #       pregunta al usuario la ubicion el archvo que tiene la letra y lo lee
        #   generar_lista_parrafos()
        #   volver a main.py
        os.system("clear") # despues crear una funcion limpiar_terminal() que tenga un os.system("*") para cada os popular
        print("crear archivo")
        archivo = input("Ingrese la ruta de la letra en texto plano [ej: ~/Music/letra.txt]: ")
        print(archivo)
        input()
        main()
    elif opcion == '2':
        os.system("clear")
        # header() (print opciones)
        # if !cancion_terminada
        #    enter -> escribit_linea_en_archivo()
        #               linea + linea + 1
        #               print(lista[contador])
        #               agregar al archivo timer actual + parrafo de la lista
        #

        print("Vas a generar tu archivo .lrc")
        print("Tené a mano un reproductor con tu canción, y la empieces a reproducir presioná enter en este programa")
        print("Cada vez que se escuche entonar la estrofa que aparece por pantalla, precioná enter")
        print("Si te equivocaste, y querés reiniciar la generación del archivo, precioná (r) seguido de enter")
        print("Cuando la canción termine de reproducirse precioná (t) seguido de enter")
        print("")
        accion = 0
        while accion != "q":
            accion = input("Acción elegida: ")
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

