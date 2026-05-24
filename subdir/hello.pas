{ 2026-05-24 }
program hello;
uses
    SysUtils;
begin
    writeln('Hello world');
    try
        writeln(FormatDateTime('yyyy-mm-dd', Date));
    except
        writeln('none');
    end;
end.
