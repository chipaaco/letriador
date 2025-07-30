# user crt
La libreria **crt** es una biblioteca estandar que proporciona funciones para el control de la consola y la pantalla. Su nombre significa "Console Run Time" y es muy util para crear programas interactivos en la consola.

1. Control de pantalla
> ClrScr - Limpia la pantalla.

> GotoXY(x, y) - Mueve el cursor a una posicion especifica.

> WhereX y WhereY - Obtienen la posicion actual del cursor.

2. Colores y Formato
> TextColor(color) - Cambia el color del texto.

> TextBackground(color) - Cambia el color de fondo.

> HighVideo y LowVideo - Cambian la intensidad del texto.

3. Entrada de teclado
> ReadKey - Lee una tecla sin mostrar el caracter

> KeyPressed - Verifica si se presiono una tecla

```bash
uses crt;

begin
    ClrScr;                     #// Limpia la pantalla
    TextColor (Red);            #// Cambia color del texto a rojo
    GotoXY (10, 5);             #// Mueve cursor a posicion (10, 5)
    WriteLn ('Hola Mundo!');
    Delay (1000);               #// Espera 1 segundo
    TextColor (White);          #// Vuelve al color blanco
end.
```
