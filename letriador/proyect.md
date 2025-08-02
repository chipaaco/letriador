# LRC Generator
## Que es?
Un archivo LRC (.lrc) es un archivo de letra sincronizada que se usa en reproductores de musica para mostrar la letra a medida que avanza la cancion.

## Un .lrc tiene:
- Opcionalmente, informacion de la cancion (titulo, artista, etc).
- Una letra dividida en lineas.
- Cada linea tiene una marca de tiempo asociada (cuando se canta esa parte).

Por ejemplo:
> [00:12.00] Esto es la primera linea.
> [00:18.50] Y esta es la segunda.

- Pensar en el flujo general del programa:

1. Te deje escribir la letra (linea por linea)
2. Para cada linea, **te pregunte en que momento se canta** (minutos, segundos, centesimas)
3. Genere un archivo con el formato [mm:ss.xx] linea
4. Guarde todo eso en un archivo .lrc

---

# Para contruir el programa (Aplicacion):
Me debo imaginar las tareas como partes del programa

- Preguntarme:
- Como voy a almacenar cada linea de la letra?
- Como voy a guardar los tiempos para cada linea?
- Como voy a unir el tiempo con la linea?
- Como voy a guardar eso en un archivo de texto?

# Idea por donde empezar:
- Escribir una sola linea con tiempo manual
- Mostrarla en pantalla con el formato **[mm:ss.xx] linea**
- Luego repetir con varias lineas
- Y finalmente guardar en un archivo
- **Puedo probar creando archivos reales**.
- Crear un .lrc a mano en un bloc de notas
- Abrirlo con algun reproductor que soporte letras sincronizadas (VLC con plugin).
- Ver como se comporta
- Compararlo con lo que vos generas desde tu programa.

# Pensar en hacerlo mas comodo:
Como vas a ingresar letras y tiempos, pensá:

- Te gustaría que el programa te muestre cada línea para recordarla?

- Preferís ingresar todo junto o ir uno por uno?

- Te gustaría que el programa guarde metadatos (nombre del artista, etc.)?

# Como organizo mi idea?
- Descomponer un **Problema** en tareas mas pequeñas y manejable:
- Analisis del Problema Completo.

1. Primero entender que quiero lograr.
- Objetivo: Crear un programa que genere archivos LRC.
- Entrada: Letra + Tiempo. ```Porque como entrada la letra y el tiempo?```
- Salida: Archivo .lrc con formato [mm:ss.xx] linea.

2. Identificar las Funciones Principales.

Primer paso:
- **Que acciones principales debe hacer mi programa?**
1. Recibir entrada (letra y tiempo).
2. Procesar datos (formatear).
3. Generar salida (archivo .lrc)

Segundo paso:
- **Dividir cada Funcion en Sub-Tareas**
Funcion "A1": Recibir Entrada
- Como voy a pedir la letra?
- Como voy a pedir los tiempos?
- Como voy a almacenar estos datos?

Funcion "A2": Procesar Datos
- Como voy a convertir tiempo a formato [mm:ss.xx]?
- Como voy a unir tiempo con linea?
- Como voy a validar que los datos sean correctos?

Funcion "A3": Generar Salida
- Como voy a crear el archivo?
- Como voy a escribir en el archivo?
- Que formato exacto necesito?

3. Orden de Prioridad
**"Lo mas simple primero"**
- Empazar con lo basico: Una sola linea.
- Luego agregar complejidad: Multiples lineas.
- Finalmente optimizar: Interfaz, validaciones, etc.









# Pseudocodigo
## Pseudocodigo del Programa LRC
INICIO DEL PROGRAMA

1. Mostrar la pantalla principal con el título y las opciones:
      1: Cargar letra al programa
      2: Generar archivo LRC
      3: Ayuda
      4: Salir

2. Pedir al usuario que elija una opción

3. SEGÚN la opción elegida HACER:
      SI opción = 1 ENTONCES
          → LLAMAR a procedimiento CARGAR_LETRA
          → Volver al menú principal

      SI opción = 2 ENTONCES
          → LLAMAR a procedimiento GENERAR_LRC
          → Volver al menú principal

      SI opción = 3 ENTONCES
          → Mostrar la explicación de qué es un archivo LRC
          → Esperar que el usuario presione una tecla
          → Volver al menú principal

      SI opción = 4 ENTONCES
          → Mostrar "¡Gracias por usar!"
          → TERMINAR el programa

      EN CUALQUIER OTRO CASO
          → Mostrar "Opción no válida"
          → Volver al menú principal

## Procedimiento CARGAR_LETRA

1. Mostrar: "Pegá o escribí la letra de la canción. Presioná Ctrl+D o Ctrl+Z para finalizar."

2. Crear una LISTA llamada LETRA vacía.

3. Mientras el usuario escriba líneas HACER:
      → Leer la línea
      → Agregar la línea a la lista LETRA

4. Mostrar en pantalla la lista completa de versos cargados.

5. Preguntar: "¿Querés volver a intentarlo porque te equivocaste? (s/n)"
      SI respuesta = "s" ENTONCES
          → Volver a CARGAR_LETRA
      SI respuesta = "n" ENTONCES
          → Salir y volver al menú principal

## Procedimiento GENERAR_LRC

1. Mostrar instrucciones:
      - Reproducí la canción
      - Presioná ENTER cuando se cante cada verso
      - Presioná "r" para reiniciar
      - Presioná "t" cuando termine la canción
      - Presioná "q" para salir

2. Crear un contador de verso = 0

3. Mientras el usuario no presione "q" HACER:
      → Mostrar el verso actual de la lista LETRA[contador]
      → Leer lo que presiona el usuario:

          SI presiona ENTER ENTONCES
              - Registrar el tiempo (HH:MM:SS)
              - Guardar el verso con el tiempo en el archivo LRC
              - Avanzar al siguiente verso

          SI presiona "r" ENTONCES
              - Preguntar: "¿Seguro que querés reiniciar? (s/n)"
              - Si dice "s", borrar lo que se haya generado y volver a empezar
              - Si dice "n", seguir normalmente

          SI presiona "t" ENTONCES
              - Terminar de generar el archivo
              - Mostrar la ubicación del archivo .lrc
              - Salir del procedimiento

