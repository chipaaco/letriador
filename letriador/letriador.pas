Program letriador;
{AMBIENTE}
uses crt;

var 
//--------
{MENU}
num_opciones: integer; // Variable numero de opciones

{Procedimiento CargarLetra}
letras_verso: array[1..500] of string; // 500 lineas maximo
linea_actual : string; // Linea que se esta escribiendo
num_lineas: integer; // Contador de lineas
bandera: boolean; // Verifica si se presiono 'E'
//--------

{Procedimiento: Cargar Letra}
procedure CargarLetra (void);
    {Declaraciones Locales}

begin
    num_lineas := 0; // Se inicializa a 0 para ver cuantas lineas hay y poder saber cual es la que va despues...
    WriteLn('Cargar la Letra de la Cancion:');
    WriteLn('Pega o escribir aca el contenido de la letra que hayas encontrado en internet y luego presiona "E" para guardarlo');
    {Numero de lineas: Contador}
    num_lineas := num_lineas +1;    
    ReadLn(linea_actual); // Lee lo que escribio el usuario
    letras_verso[num_lineas] := linea_actual; // Lo guarda en el array
end; 

{Procedimiento: Verificar si esta cargada}
procedure Verification (void);
begin

end;

{Procedimiento: Sincronizar (marcar tiempos)}
procedure SincronizatorTime (void);
begin
end; 

{Procedimiento: Guardar LRC}
procedure SaveLRC (void);
begin
end;




{PROCESO}
begin
    {Una vez que termina cualquiera de las opciones (carga letra o sincronizar), volves al menu principal. Esto lo resolverias con un bucle}
    while num_opciones <> 4 do
        begin
            {MENU}
            WriteLn(' _      _        _           _');
            WriteLn('| | ___| |_ _ __(_) __ _  __| | ___  _ __');
            WriteLn('| |/ _ \ __| __ | |/ _` |/ _` |/ _ \| __|');
            WriteLn('| |  __/ |_| |  | | (_| | (_| | (_) | |');
            WriteLn('|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|');
            WriteLn('Cargar la letras');
            {OPCIONES}
            WriteLn('Seleccione una Opcion, porfavor: ');
            WriteLn('1: Cargar letra al programa');
            WriteLn('2: Sincronizar (marcar tiempos con ENTER)'); {Sincronizacion con la cancion}
            WriteLn('3: Ayuda!');
            WriteLn('4: Salir'); {Preguntar si esta seguro salir o no}
            ReadLn(num_opciones); {Colocar el numero}
            Write('La opcion que elegiste es ');

            if num_opciones = 1 then
                WriteLn('Opcion 1'); 
            if num_opciones = 2 then
                WriteLn('Opcion 2');
            if num_opciones = 3 then
                WriteLn('Opcion 3');
            {Opcion del (SALIR)}
            if num_opciones = 4 then
                WriteLn('Opcion 4');
                break;
            else 
                WriteLn('La opcion que elegiste no es correcta');
        end;
end.
{1. Cargar la letra de una cancion}
{2. Verificar si ya esta cargada}
{3. Mostrar la letra linea por linea mientras vos marcas el tiempo (ENTER)}
{4. Guardar el archivo en un .lrc con los tiempos}
{5. Volver al menu principal}

// 1. Pedir al usuario que pegue/escriba la letra
// 2. Leer línea por línea
// 3. Almacenar cada línea
// 4. Cuando presione "E" → terminar de cargar
// 5. Guardar la letra completa en memoria





