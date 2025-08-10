**Metodo Secuencial**:

**Metodo Biseccion o busqueda binaria**:
Se va partiendo por la mitad la lista en consideracion hasta que queda vacia en el peor de los casos. Esto varia segun log2n. En una busqueda binaria nunca se necesitarian mas de log2(n**50.000**), que es alrededor de 16.
# Conceptos en la Programacion Estrucutrada:
**FIABILIDAD**:
**EFICIENCIA**:
**CLARIDAD**:

**SIMPLICIDAD**:
Un progama simple es mas facil de modificar y ello adquiere importancia en la fase de mantenimientos de las aplicaciones.

**MODULARIDAD**:
La mayor parte de los programas largos se pueden dividir en un conjunto de subtareas identificables. A estas subtareas en *PASCAL* se las llama "PROCEDIMIENTOS" o "FUNCIONES".

**GENERALIDAD**:
Generalidad considerable y suficiente con muy poco esfuerzo de programacion adicional. Por tanto conviene que esta sea una tendencia.

**TRANSPORTABILIDAD**:
El grado de transportabilidad optimo se consigue utilizando un compilador ajustado a normas estadar y renunciando a las extensiones de mejora introducidas por el fabricante.

# ELEMENTOS BASICOS:
Un progama en PASCAL es un conjunto de instrucciones o sentencias, escritas segun ciertas reglas, para realizar operaciones sobre entidades de datos conocidas como constantes, variables y resultados de funciones.

# EL CONCEPTO DE TIPO DE DATOS:
Existen las EXPRESIONES que corresponden algun tipo siempre.
Estos pueden ser entero o reales. Las operaciones relacionales y logicas producen valores Booleanos.

Comentarios en Pascal: **{Algo}, (* *)**
Puntero: **@, ^**
Operador de Subrango: **..**

# Significado de Abreviaturas:
nul: nulo
ht: tabulador horizontal
cr: retorno de carro
bel: campana
nl: salto de linea
esc: escape
bs: retroceso
vs: tabulador vertical

Observaciones:
• Los códigos de los caracteres 0 a 31 y 127 no son imprimibles
• Los códigos de las letras mayúsculas, los de las minúsculas y los de las cifras son
contiguos entre sí.
• La diferencia entre una letra mayúscula y su correspondiente minúscula es 32.








## Guia mental/ patron:

- Sabes cuantas veces se repite(ej: 10 veces) 
    **FOR**.
- No sabes cuantas veces, pero tenes una condicion para parar (ej: hasta que el usuario escriba "salir"). 
    **WHILE o REPEAT...UNTIL**.
- Necesitas que almenos una vez se ejecute el bloque, incluso si despues la condicion no se cumple. 
    **REPEAT...UNTIL**
