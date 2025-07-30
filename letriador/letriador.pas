Program letriador;
{AMBIENTE}
uses crt;

var 
letras: string;
tecla : char;
num_opciones: integer;

{Procedimiento: Cargar Letra}
procedure CargarLetra (void);
{Declaraciones Locales}
begin
    WriteLn('Crear una Lista');
    WriteLn('Pega o escribir aca el contenido de la letra que hayas encontrado en internet y luego presiona "E" para guardarlo');
    {Crear una lista para almacenar toda la letra completa}
    lista_letra: 
    if 
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
    WHILE num_opciones <> 4 DO
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
        else 
            WriteLn('La opcion que elegiste no es correcta');
end.
{1. Cargar la letra de una cancion}
{2. Verificar si ya esta cargada}
{3. Mostrar la letra linea por linea mientras vos marcas el tiempo (ENTER)}
{4. Guardar el archivo en un .lrc con los tiempos}
{5. Volver al menu principal}






