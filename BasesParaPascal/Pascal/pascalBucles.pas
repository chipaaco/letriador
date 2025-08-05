//  Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
// - Una cadena de texto que representa una fecha tiene el formato:
// "dd/MM/yyyy"
// Esto es un String y devolvera un int
// - La función recibirá dos String y retornará un Int.
// - La diferencia en días será absoluta (no importa el orden de las fechas).

// Condicion
// - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

program pascalAprendizaje;

var
    contador, x, salida : Integer; 
begin
    ReadLn(contador);
    For x:=0 to contador do 
        begin
            Write('Va por el:');
            WriteLn(x);
        end;
    WriteLn('Terminado');

// Cuenta Regresiva del 1 al 0
    ReadLn(contador);
    For x:=100 downto contador do
        begin
            Write('Va por el:');
            WriteLn(x);
        end;

// Bucle repite hasta que sea verdadera y se sale cuando es falso 
repeat
    Write('Introduce un numero entre el (0..9): ');
    ReadLn(salida);
until (salida >= 0) and (salida <= 9);
WriteLn('Por fin un valor correcto, terminado');

// Esto es un while do
Write('Introduce un numero: '); ReadLn(contador);
x := 0;
while x <> contador do 
begin
    WriteLn(x);
    x := x + 1;
end;

// Este es su reves
Write('Introduce un numero: '); ReadLn(contador);
x := 100;
while x <> contador do 
begin
    WriteLn(x);
    x := x + 1;
end;




end.












