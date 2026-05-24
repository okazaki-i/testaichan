! 2026-05-24
program hello
    character(len=10) :: date
    character(len=8) :: time
    integer :: values(8), stat

    print *, "Hello World !!"
    call date_and_time(date=date, time=time, values=values)
    stat = values(1)
    if (stat > 0) then
        print *, date(1:4) // "-" // date(5:6) // "-" // date(7:8) // " " // time(1:2) // ":" // time(3:4) // ":" // time(5:6)
    else
        print *, "none"
    end if
end program hello
