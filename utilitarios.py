import os

def limpiar():
    #Limpia la terminal para cualquier sistema operativo.
    if os.name == 'nt':
        os.system('cls') # si el sistema es windows
    else:
        os.system('clear') # si el sistema se parece a UNIX (linux o mac)

def mostrar_estatus(estatus):
    # Muestra un mensaje descriptivo del estatus actual del programa.
    # Recibe el estatus como parámetro.
    texto = "Estatus: "
    if estatus == 0:
        print(texto + "la letra todavía no se carga")
    elif estatus == 1:
        print(texto + "la letra está cargada")
    elif estatus == 2:
        print(texto + "archivo .lrc generado con éxito")
    else:
        print("Error: estatus desconocido -> " + str(estatus))
