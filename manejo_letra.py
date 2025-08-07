from utilitarios import limpiar

def formatear_letra(letra_bruta):
    # función interna para limpiar la lista de versos.
    # Elimina líneas vacías y espacios al inicio/final.
    lista_arreglada = []
    for verso in letra_bruta:
        # strip() srive para eliminar espacios en blanco y saltos de línea (https://docs.python.org/3/library/stdtypes.html#str.strip)
        # append() agrega elementos al final de una lista
        if verso.strip() != "":
            lista_arreglada.append(verso.strip())
    return lista_arreglada

def cargar_letra():
    # gestiona la entrada del usuario para cargar la letra de la canción.
    # no usa variables globales, devuelve la letra cargada y un nuevo estatus.
    letra_cargada = []
    
    while True: # Bucle para permitir reintentos
        limpiar()
        print(r"""Cargar Letra:

Pegá o escribí acá el contenido de la letra...

después apretá Ctrl + D (Linux/macOS) o Ctrl + Z y Enter (Windows) para guardarlo.
        """)
        
        buffer_letra = []
        while True:
            # try y except son la forma en que python maneja errores (https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
            try:
                verso = input()
                buffer_letra.append(verso) # .append agrega verso al final del buffer (lista temporal)
            except EOFError:
                # en este caso queremos que ocurra el error EOF para salir del input() al terminar de cargar (https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
                break
        
        letra_cargada = formatear_letra(buffer_letra)
        
        print("\n\nLa lista generada es:")
        print(letra_cargada)
        print("")
        
        satisfaccion = input("¿Estás satisfecho/a? (Enter para continuar, o 'r' para reiniciak): ")
        if satisfaccion.lower() != "r":
            input("\nPerfecto, letra guardada. Apretá Enter para volver al menú principal...")
            # Devolvemos la letra cargada y el nuevo estatus (1 = cargada)
            return letra_cargada, 1
        
        input("\nEntendido, volvamos a cargar la letra. Presioná Enter...")
