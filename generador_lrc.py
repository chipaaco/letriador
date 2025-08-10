import os
import time
from utilitarios import limpiar

def generar_txt(letra, estatus_actual):
    # Genera el archivo .txt sincronizando la letra proporcionada.
    # Recibe la letra y el estatus como parámetros.
    # Devuelve el nuevo estatus del programa.
    if estatus_actual == 0:
        print("no se puede generar nada si no se carga una letra primero")
        input("Apretá Enter para volver al menú...")
        return estatus_actual

    print("Generar Archivo .txt:\n")
    nombre_archivo = input("¿Cómo se llama el archivo de música? (ej: tinta_roja.mp3): ")
    if not nombre_archivo:
        print("Nombre mal puesto")
        input("Apretá Enter para continuar...")
        return estatus_actual

    nombre_base, _ = os.path.splitext(nombre_archivo) # cancion.mp3 -> cancion, mp3 (https://docs.python.org/3/library/os.path.html#os.path.splitext)
    # _ es una convencion cuando no nos interesa la variable
    nombre_archivo_txt = nombre_base + ".txt"

    limpiar()
    print("El archivo se guardará como: " + nombre_archivo_txt)
    print("")
    print("PREPARATE!")
    print("Reproducí tu canción en un reproductor externo.")
    input("Apenas empiece la música, apretá Enter para iniciar el cronómetro...")

    cronometro = time.time()
    indice_verso = 0
    nuevo_estatus = estatus_actual

    # inicializar archivo para escritura
    with open(nombre_archivo_txt, 'w', encoding='utf-8') as archivo_txt:
        # with gestiona el contexto del archivo
        print("\nArrancó el cronómetro y el archivo "+ nombre_archivo_txt + " fue creado.")
        print("---")
        print("")


        # --- BUCLE PRINCIPAL del lector ---


        while indice_verso < len(letra):
            limpiar()
            print("Sincronizando: "+ nombre_archivo)
            # leer archivo sin un gestor de contexto
            incompleto_txt = open(nombre_archivo_txt, 'r')
            print(incompleto_txt.read())
            incompleto_txt.close()
            print("---")
            print("VERSO ACTUAL: (", indice_verso + 1, "/", len(letra), ")")
            print(letra[indice_verso])
            print("---")
            print("apretá Enter para grabar el tiempo de este verso.")
            print("Escribí 'r' para reiniciar o 'q' para cancelar y salir.")
            
            accion = input("Acción: ").lower()

            if accion == '':
                tiempo_transcurrido = time.time() - cronometro
                minutos = int(tiempo_transcurrido / 60)
                segundos = int(tiempo_transcurrido % 60)
                centesimas = int((tiempo_transcurrido - int(tiempo_transcurrido)) * 100)
                timestamp = f"[{minutos:02d}:{segundos:02d}.{centesimas:02d}]" # 02d -> f-string con dos digitos, con 0 si no hay nada
                
                linea_completa = timestamp + letra[indice_verso] + "\n"

                # escribir archivo
                archivo_txt.write(linea_completa) #escribe en el buffer
                archivo_txt.flush() #forzar escritura archivo
                
                indice_verso += 1

            elif accion == 'r':
                print("\nReiniciando...")
                # salimos con return y la función se vuelve a llamar desde el menu principal
                return generar_txt(letra, estatus_actual) 

            elif accion == 'q':
                print("\nGrabación cancelada por el usuario.")
                break
        
        if indice_verso == len(letra):
            limpiar()
            print("TODO LISTO!")
            print("sincronizast todos los versos de la canción")
            nuevo_estatus = 2
        else:
            print("\nProceso finalizado antes de completar todos los versos.")

    input("\napretá Enter para volver al menú principal...")
    return nuevo_estatus
