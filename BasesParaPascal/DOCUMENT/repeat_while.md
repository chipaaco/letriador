**Tiene una gran diferencia entre el while do y este repeat until**
# La diferencia esta en que:

## "El BUCLE repeat ... until
    - Se evalua al final del bloque.
    - Siempre se ejecuta almenos una vez.
    - Se repite hasta que sea verdadera.

## 
    - Hace el chequeo de la condicion al pricipio, y puede evitar usar bloque si solo hay una instruccion. 

```bash
// Bucle repite hasta que sea verdadera y se sale cuando es falso

repeat
    Write('Introduce un numero entre el (0..9): ');
    ReadLn(salida);
until (salida>=0) and (salida<=9);
WriteLn('Por fin un valor correcto, terminado');
```