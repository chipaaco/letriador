program GeneradorLRC;

uses crt, sysutils;

var
  letra: array of string;
  opcion, accion, seguro, verso: string;
  i: integer;

procedure limpiar();
begin
  ClrScr;
end;

procedure cargar_letra();
begin
  writeln('crear una lista');
  writeln('Pegá o escribí acá el contenido de la letra que hayas encontrado en internet y luego apretá Ctrl-D o Ctrl-Z para guardarlo.');
  writeln('');

  SetLength(letra, 0);

  while not eof(input) do
  begin
    readln(verso);
    SetLength(letra, Length(letra) + 1);
    letra[High(letra)] := verso;
  end;

  writeln('');
  write('[');
  for i := 0 to High(letra) do
  begin
    if i > 0 then
      write(', ');
    write('"', letra[i], '"');
  end;
  writeln(']');
  readln;
end;

procedure generar_lrc();
begin
  writeln('Vas a generar tu archivo .lrc');
  writeln('Tené a mano un reproductor con tu canción, y la empieces a reproducir presioná enter en este programa');
  writeln('Cada vez que se escuche entonar la estrofa que aparece por pantalla, precioná enter');
  writeln('Si te equivocaste, y querés reiniciar la generación del archivo, precioná (r) seguido de enter');
  writeln('Cuando la canción termine de reproducirse precioná (t) seguido de enter');
  writeln('Cuando la cancion termine presiona Q');
  writeln('');

  accion := '0';
  while LowerCase(accion) <> 'q' do
  begin
    write('Acción elegida: ');
    readln(accion);
    if accion = '' then
    begin
      writeln('mostrar linea agregada al archivo .lrc [00:00:00] verso que se esta cantando');
      accion := '0';
    end
    else if LowerCase(accion) = 'r' then
    begin
      write('estas seguro que queres reiniciar? todo el progreso se perdera (s/n)');
      readln(seguro);
      accion := '0';
      if LowerCase(seguro) = 's' then
      begin
        exit; // vuelve al main
      end
      else if LowerCase(seguro) = 'n' then
      begin
        writeln('ok, no paso nada entonces');
      end;
    end;
  end;
end;

procedure main();
begin
  limpiar();
  writeln(' _      _        _           _');
  writeln('| | ___| |_ _ __(_) __ _  __| | ___  _ __');
  writeln('| |/ _ \ __| ''__| |/ _` |/ _` |/ _ \| ''__|');
  writeln('| |  __/ |_| |  | | (_| | (_| | (_) | |');
  writeln('|_|\___|\__|_|  |_|\__,_|\__,_|\___/|_|');
  writeln('');
  writeln('Estatus: la letra todavia no se carga');
  writeln('');
  writeln('Opciones:');
  writeln('1: cargar letra al programa');
  writeln('2: generar archivo lrc');
  writeln('3: ayuda');
  writeln('4: salir');
  writeln('');
  write('Elija una opción: ');
  readln(opcion);

  if opcion = '1' then
  begin
    limpiar();
    cargar_letra();
    main();
  end
  else if opcion = '2' then
  begin
    limpiar();
    generar_lrc();
    main();
  end
  else if opcion = '3' then
  begin
    writeln('');
    writeln('¿Que es un archivo lrc?');
    writeln('');
    writeln('Es un archivo que comparte la misma ruta y nombre que un archivo de audio (mp3, flac, wav, etc), contiene el momento exacto en que se canta una estrofa en una canción. Una característica es que su archivo termina con la extensión .lrc.');
    writeln('');
    write('Precioná cualquier tecla para volver al inicio: ');
    readln;
    main();
  end
  else if opcion = '4' then
  begin
    writeln('¡Gracias por usar!');
  end
  else
  begin
    write('Opción no válida. Apretá Enter para continuar...');
    readln;
    main();
  end;
end;

begin
  main();
end.
