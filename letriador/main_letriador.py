# LETRIADOR
# -- Librería estándar
import os
import time

# --- SISTEMA DE DECORADORES PARA FUNCIONES ---

# Diccionario para almacenar las funciones registradas
funciones_disponibles = {}

def registrar_funcion(nombre, descripcion=""):
    """Decorador para registrar funciones en el sistema."""
    def decorador(func):
        funciones_disponibles[nombre] = {
            'funcion': func,
            'descripcion': descripcion,
            'nombre': nombre
        }
        return func
    return decorador

def llamar_funcion(nombre, *args, **kwargs):
    """Llama una función registrada por su nombre."""
    if nombre in funciones_disponibles:
        return funciones_disponibles[nombre]['funcion'](*args, **kwargs)
    else:
        print(f"Error: La función '{nombre}' no está registrada.")
        return None

def listar_funciones():
    """Muestra todas las funciones registradas."""
    print("\n--- FUNCIONES DISPONIBLES ---")
    for nombre, info in funciones_disponibles.items():
        print(f"• {nombre}: {info['descripcion']}")
    print("-" * 30)

# --- VARIABLES GLOBALES ---
letra = []
estatus = 0 # 0: Inicio, 1: Letra cargada, 2: LRC generado

# --- Funciones Utilitarias ---

@registrar_funcion("limpiar", "Limpia la terminal de cualquier sistema operativo")
def limpiar():
    """Limpia la terminal de cualquier sistema operativo."""
    if os.name == 'nt':
        os.system('cls')  # si el sistema es windows
    else:
        os.system('clear')  # si el sistema se parece a UNIX

@registrar_funcion("mostrar_estatus", "Muestra el estado actual del proceso")
def mostrar_estatus():
    """Muestra el estado actual del proceso."""
    texto = "Estatus: "
    if estatus == 0:
        print(texto + "La letra todavía no se carga.")
    elif estatus == 1:
        print(texto + "La letra está cargada, lista para generar el TXT.")
    elif estatus == 2:
        print(texto + "Archivo TXT generado con éxito.")
    else:
        print("Algo mal con la variable estatus: " + str(estatus))

# --- Funciones #1: generar letra del programa ---

@registrar_funcion("formatear_letra", "Elimina las líneas vacías de la letra")
def formatear_letra(letra_descuageringada):
    """Elimina las líneas vacías de la letra."""
    lista_arreglada = []
    for verso in letra_descuageringada:
        if verso.strip() != "":
            lista_arreglada.append(verso.strip())
    return lista_arreglada

@registrar_funcion("cargar_letra", "Permite al usuario pegar la letra y la guarda")

def cargar_letra():
    """Permite al usuario pegar la letra y la guarda en la variable global."""
    print("Pegá o escribí acá la letra y luego apretá Ctrl+D (Linux/Mac) o Ctrl+Z y Enter (Windows) para guardar.")
    print("-" * 30)

    # La variable global 'letra' se reinicia para una nueva carga
    global letra
    letra = []
    
    # Bucle para leer múltiples líneas de input
    while True:
        try:
            verso = input()
            letra.append(verso)
        except EOFError:
            break
    
    letra = formatear_letra(letra)
    print("\n--- Letra Cargada ---")
    for l in letra:
        print(l)
    print("-" * 21)
    
    print("\n¿Estás satisfecho/a?")
    satisfaccion = input("Presioná cualquier tecla para continuar, o (r) para volver a cargar: ")
    if satisfaccion.lower() == "r":
        input("Entendido, volvamos a cargar la letra")
        limpiar()
        cargar_letra()
    else:
        global estatus # para modificar la variable que esta afuera de la función
        estatus = 1
        input("Perfecto, ahora podés continuar generando el .txt")

# --- Funciones #2: generar archivo .lrc ---

@registrar_funcion("formatear_tiempo", "Convierte segundos a formato de tiempo LRC")
def formatear_tiempo(segundos):
    """Convierte segundos (float) a formato de tiempo LRC [mm:ss.xx]"""
    minutos = int(segundos / 60)
    segundos_restantes = segundos % 60
    # .xx se refiere a centésimas de segundo
    centisegundos = int((segundos_restantes - int(segundos_restantes)) * 100)
    return f"[{minutos:02d}:{int(segundos_restantes):02d}.{centisegundos:02d}]"

@registrar_funcion("generar_lrc", "Genera el archivo .txt usando input() estándar")
def generar_lrc():
    """Genera el archivo .txt usando input() estándar."""
    global estatus
    if estatus != 1:
        print("No se puede generar nada si no se carga una letra primero (Opción 1).")
        input("Presioná Enter para volver al menú...")
        return

    print("Vas a generar tu archivo .txt")
    nombre_archivo = input("¿Cómo se llama el archivo de música? (ej: tinta_roja.mp3): ")
    if not nombre_archivo:
        input("El nombre no puede estar vacío. Presioná Enter para volver...")
        return
        
    # Aseguramos que el archivo TXT tenga el nombre correcto
    nombre_base = os.path.splitext(nombre_archivo)[0]
    nombre_archivo_txt = nombre_base + ".txt"

    limpiar()
    print("Preparate para sincronizar. Vas a usar un reproductor externo.")
    print("\n--- INSTRUCCIONES ---")
    print("1. Empezá a reproducir tu canción.")
    print("2. Presioná ENTER justo cuando se cante el primer verso que cargaste.")
    print("3. Seguí presionando ENTER para cada verso siguiente.")
    print("\n--- TECLAS ---")
    print(" - [Enter]: Grabar el tiempo del verso actual.")
    print(" - [R]:     Reiniciar la grabación desde cero.")
    print(" - [Q]:     Finalizar y guardar el archivo TXT.")
    
    input("\nPresioná Enter cuando estés listo para empezar...")

    limpiar()

    # --- Lógica principal de grabación ---
    indice_verso = 0
    lineas_generadas = []
    
    print("Esperando el inicio de la canción... (Presioná Enter para empezar el contador)")
    input() # Espera a que se presione Enter por primera vez
    
    tiempo_inicio = time.perf_counter() # ¡El contador empieza AHORA!

    while indice_verso < len(letra):
        limpiar()
        tiempo_transcurrido = time.perf_counter() - tiempo_inicio
        
        print(f"Generando: {nombre_archivo_txt}")
        print(f"Tiempo corriendo: {formatear_tiempo(tiempo_transcurrido)}")
        print("-" * 30)
        print("ÚLTIMA LÍNEA GRABADA:")
        print(lineas_generadas[-1] if lineas_generadas else "Ninguna todavía.")
        print("-" * 30)
        print("PRÓXIMO VERSO A GRABAR:")
        print(f"==> {letra[indice_verso]}")
        print("-" * 30)
        print("[Enter] Grabar | [R] Reiniciar | [Q] Finalizar y Guardar")

        # Usamos input() estándar en lugar de keyboard
        accion = input("Acción: ").lower().strip()

        if accion == "" or accion == "enter":
            tiempo_grabado = time.perf_counter() - tiempo_inicio
            linea_formateada = f"{formatear_tiempo(tiempo_grabado)} {letra[indice_verso]}"
            lineas_generadas.append(linea_formateada)
            indice_verso += 1
        
        elif accion == "r":
            print("Reiniciando la grabación...")
            time.sleep(1) # Pausa para que el usuario lea el mensaje
            # Llamada recursiva para empezar de nuevo
            generar_lrc() 
            return # Salimos de la ejecución actual

        elif accion == "q":
            print("Grabación finalizada por el usuario.")
            time.sleep(1)
            break # Sale del bucle while

    # --- Fin del bucle, ahora a guardar el archivo ---
    if lineas_generadas:
        try:
            with open(nombre_archivo_txt, 'w', encoding='utf-8') as archivo:
                archivo.write("\n".join(lineas_generadas))
            limpiar()
            print("¡Éxito! Archivo TXT guardado.")
            print(f"Nombre: {nombre_archivo_txt}")
            print("\n--- Contenido Generado ---")
            for linea in lineas_generadas:
                print(linea)
            print("\n--------------------------")
            estatus = 2
        except Exception as e:
            print(f"Ocurrió un error al guardar el archivo: {e}")
    else:
        print("No se grabó ninguna línea, no se generó el archivo.")

    input("\nPresioná Enter para volver al menú principal...")

# --- FUNCIÓN PRINCIPAL ---

@registrar_funcion("main", "Función principal del programa")
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
    print("1: Cargar letra al programa")
    print("2: Generar archivo .txt")
    print("3: Ayuda")
    print("4: Listar funciones registradas")
    print("5: Ejecutar función por nombre")
    print("6: Salir")
    print("")

    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiar()
        cargar_letra()
        main()
    elif opcion == '2':
        limpiar()
        generar_lrc()
        main()
    elif opcion == '3':
        limpiar()
        print("--- ¿Qué contiene el archivo .txt generado? ---\n")
        print("Es un archivo de texto simple que sincroniza las letras con una canción.")
        print("Cada línea contiene una marca de tiempo (ej. [00:23.45]) seguida del verso correspondiente.")
        print("Podés abrirlo con cualquier editor de texto o usarlo como base para otros formatos.")
        print("\nEl contenido mantiene el formato de marcas de tiempo estilo LRC.")
        input("\nPresioná cualquier tecla para volver al inicio: ")
        main()
    elif opcion == '4':
        limpiar()
        listar_funciones()
        input("\nPresioná Enter para volver al menú...")
        main()
    elif opcion == '5':
        limpiar()
        print("--- EJECUTAR FUNCIÓN POR NOMBRE ---")
        listar_funciones()
        nombre_funcion = input("\nIngresa el nombre de la función a ejecutar: ").strip()
        if nombre_funcion in funciones_disponibles:
            print(f"\nEjecutando: {nombre_funcion}")
            llamar_funcion(nombre_funcion)
        else:
            print(f"La función '{nombre_funcion}' no existe.")
        input("\nPresioná Enter para volver al menú...")
        main()
    elif opcion == '6':
        print("\n¡Gracias por usar!")
        time.sleep(2)
        limpiar()
    else:
        input("Opción no válida. Apretá Enter para continuar...")
        main()

if __name__ == "__main__":
    main()