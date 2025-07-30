// fpc pascal.pas
// ./pascal

// https://github.com/cfenollosa/os-tutorial
// https://littleosbook.github.io/
// Crear un Bootloader

// - type se usa para definir tipos de datos, mientras que const se usa para definir valores constantes.
// Se pueden definir del 1..200 por ejemplo

// Si tengo una constante es eficiente ya que en el tiempo de compilacion por su valor declarado es sustituido cada vez donde se entren usadas. Esto repercute en que el procesador del ordenador no tiene que leer una direccion de memoria, sino que el valor se encuentra directamente empotrado en el codigo. Por lo tanto es mas rapido que el acceso a memoria las constantes.

// Write: Imprime el texto y matiene el cursor en la misma linea. Esto significa que cualquier texto posterior se imprimira en la misma linea, justo despues del texto actual.

// WriteLn: Imprime el texto y luego mueve el cursor a la sieguiente linea. Esto significa que cualquier texto posterior imprimira en una nueva linea
program pascal;
const
    PI = 3.14156;
//type

var 
    radio : Integer;
    entrada : char;

begin
    //Los bucles van dentro del Proceso
    Write('Necesitas calcular la circunferencia? [S/N]:'); 
    
    ReadLn(entrada);
    
    if (entrada = 's') or (entrada = 'S') then
    begin
        Write('La circuferencia es ');
        WriteLn( 2 * PI * radio );
    end
    else
        WriteLn('No se ha calculado la circuferencia.');
end.





