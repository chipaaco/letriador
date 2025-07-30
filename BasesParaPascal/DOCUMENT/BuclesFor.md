# Bucle For to do
```bash
contar: Integer;
x: Integer;

// El x:=0 es el indice o sea en el que inicia a contar
For x:=0 to contar do 
begin
// Lo que va dentro del bucle
end
//Regresiva
For x:= 100 downto 0 do
begin
// Lo que va dentro del bucle
end

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
end.
``` 