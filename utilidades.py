import os

# Limpiar la terminal siendo agnóstico del sistema operativo.

def limpiar():
    if os.name == 'nt':
        os.system('cls') # si el sistema es windows
    else:
        os.system('clear') # si el sistema se parece a UNIX (linux o mac)

