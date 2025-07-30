def main():
    print("Vas a generar tu archivo .lrc")
    print("Tené a mano un reproductor con tu canción, y la empieces a reproducir presioná enter en este programa")
    print("Cada vez que se escuche entonar la estrofa que aparece por pantalla, precioná enter")
    print("Si te equivocaste, y querés reiniciar la generación del archivo, precioná (r) seguido de enter")
    print("Cuando la canción termine de reproducirse precioná (t) seguido de enter")
    print("Cuando la cancion termine presiona Q")
    print("")
    accion = 0
    while accion != "q":
        accion = input("Acción elegida: ")
        if accion == "":
            print("mostrar linea agregada al archivo .lrc [00:00:00] verso que se esta cantando")
            accion = 0
        elif accion == "r":
            seguro = input("estas seguro que queres reiniciar? todo el progreso se perdera (s/n)")
            accion = 0
            if seguro == "s":
                main()
            elif seguro == "n":
                print("ok, no paso nada entonces")

