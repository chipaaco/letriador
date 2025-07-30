def main():
    print("crear una lista")
    print("Pegá o escribí acá el contenido de la letra que hayas encontrado en internet y luego apretá Ctrl-D o Ctrl-Z para guardarlo.")
    print("")
    letra = []
    while True:
        try:
            verso = input()
        except EOFError:
            break
        letra.append(verso)
    print(letra)
    input()
    # deberia preguntarse si quiere volver a intentar, por si se esquivoco en la escritura
    # deberian quitarse los dobles espacios de la lista
