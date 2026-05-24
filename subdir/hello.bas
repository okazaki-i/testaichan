' 2026-05-24
PRINT "Hello world"
IF DATE$ <> "" AND TIME$ <> "" THEN
    PRINT DATE$ + " " + TIME$
ELSE
    PRINT "none"
END IF
