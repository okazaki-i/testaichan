{ 2026-05-24 }
program hello;
uses
    SysUtils;
begin
    writeln('Hello World !!');
    try
        writeln(FormatDateTime('yyyy-mm-dd hh:nn:ss', Now));
    except
        writeln('none');
    end;
end.
