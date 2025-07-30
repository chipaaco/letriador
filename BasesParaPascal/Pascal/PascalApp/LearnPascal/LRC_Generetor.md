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