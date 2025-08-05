¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
- Recuerda que todas las instrucciones de participación están en el repositorio de GitHub.
Lo primero... ¿Ya has elegido un lenguaje?
- No todos son iguales, pero sus fundamentos suelen ser comunes.
- Este primer reto te servirá para familiarizarte con la forma de participar enviando tus propias soluciones.

## EJERCICIO 1:
- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y debemos comenzar por el principio.

Respuesta: **En pascal**

## EJERCICIO 2:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

## EJERCICIO 3:
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos. (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

## EJERCICIO 4:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.

/*
 * EJERCICIO 5:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

/*
 * EJERCICIO 6:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

--- 

# Este ejercicio es de la facu
 1. Se tiene almacenado los datos de pacientes en una secuencia de caracteres
Historia clinica(4 caracteres) Nombre-TipoDeCobertura(de 10 a 29)TipoDeEspecialidad(0 a 9)Dia('L','M','V')

diseñar un algoritmo que muestre un menu con la siguientes acciones :
    - separar los datos en HistoriaClinica y Tipo de Especialidad  (no me acuerdo si eran exactamente esos dato, pero si pedia 2).
    - buscar a un paciente y si se encuentra, informar el Historia Clinica, tipo de Cobertura y Dia.
    - informar: 
        - total por tipo de especialidad y tipo de cobertura
        - el tipo de especialidad que mas se solicitó
        - el tipo de cobertura que menos se registró.
    Se puede usar la funcion CONCATENAR ----> la funcion concantena caracteres, los parametros son la variable donde guardar y el caracter a concatenar (ejemplo:= CONCATENAR (ejemplo,v)). Se usa dentro de un ciclo.

Utilizar la estructura que crea conveniente.

2. En un archivo secuencial Participantes se almacena datos de las olimpiadas (o algo asi):
PARTICIPANTES ordenado por Pais y Equipo.
    Pais | Equipo | Atleta | tiempo (seg) | Disciplina ("100m" "400m" "4x100" "4x400") | Descalificacion ("si" "no")

se pide:
- Total del tiempo por Pais, Equipo y total general de los descalificados.
- Guardar en un archivo de salida RELEVOS el Pais y Equipo si el equipo sumó un tiempo menor a 160 segundos en disciplinas ("4x100" "4x400"), tambien tienen que estar descalificados.