! 2026-05-24
program hello
    character(len=10) :: date
    integer :: values(8), stat

    print *, "Hello world"
    call date_and_time(date=date, values=values)
    stat = values(1)
    if (stat > 0) then
        print *, date(1:4) // "-" // date(5:6) // "-" // date(7:8)
    else
        print *, "none"
    end if
end program hello
