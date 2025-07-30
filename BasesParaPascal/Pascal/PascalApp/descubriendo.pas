
{ACCION}
//Nombre del programa
program descubriendo;

//Uso de las librerias
uses crt;

//Constantes Globales
const 
    PI = 3.14159265358979323846;
//Variables Globales
var
    nombre: string;
    edad: integer;

//Funciones Declaraciones, si hay algunos
// Funtion Func_Name(param...); Return_Valuel ---> Este si devuelve algo
//function Persona(Humano: boolean): string;
//begin
//    if Humano = True then
//        Persona := 'Soy un Humano';
//    else
//        Persona := 'No soy Humano';
//end;

{Procedimientos} 
procedure Saludar(nombre: string);
begin
    WriteLn(nombre);
end;

procedure Edad(edad: integer);
begin
    WriteLn(edad);
end;

{PROCESO}
begin{Inicio del programa principal}
    WriteLn(Persona(Humano));
    Saludar('Juan');
    Edad(20);
    WriteLn(PI);
    readkey;
end.{Fin del programa principal}


