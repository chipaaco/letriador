# --- MODULOS DEL PROYECTO --
from utilitarios import limpiar, mostrar_estatus
from manejo_letra import cargar_letra
from generador_lrc import generar_txt

def mostrar_ayuda():
    # Muestra la pantalla de ayuda (opción 3 del main())
    limpiar()
    print(r"""Ayuda:

¿Qué es un archivo .lrc?
Es un archivo de texto plano que contiene la letra de una canción junto con marcas de tiempo.
Los reproductores de música compatibles usan estos archivos para mostrar la letra sincronizada con la canción.
Para que funcione, el archivo .lrc debe tener el mismo nombre que el archivo de audio y estar en la misma carpeta.
Ejemplo: cancion.mp3 y cancion.lrc
""")
    input("Apreta Enter para volver al inicio...")

def main():
    # Función principal que ejecuta el bucle del programa
    letra_actual = []
    estatus_actual = 0
    
    while True:
        limpiar()
        print(r"""
 _      _        _           _
| | ___| |_ _ __(_) __ _  __| | ___  _ __
| |/ _ \ __| '__| |/ _` |/ _` |/ _ \| '__|
| |  __/ |_| |  | | (_| | (_| | (_) | |
|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|
        """)
        mostrar_estatus(estatus_actual)
        print(r"""
Opciones:
1: Cargar letra al programa
2: Generar archivo .lrc
3: Ayuda
4: Salir
        """)
        opcion = input("Elegí una opción: ")
        
        if opcion == '1':
            letra_actual, estatus_actual = cargar_letra()
        
        elif opcion == '2':
            estatus_actual = generar_txt(letra_actual, estatus_actual)

        elif opcion == '3':
            mostrar_ayuda()
        
        elif opcion == '4':
            print("\n¡Adios!")
            break
        
        else:
            input("\nOpción no válida. Apretá Enter para continuar...")

if __name__ == "__main__":
    main()
