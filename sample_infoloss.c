#include <stdio.h>

int main( void )
{
    double  a = 1.0e+16;
    double  b = 1.0;
    double  c = a + b;

    printf( "a       = %.20f\n", a     );
    printf( "b       = %.20f\n", b     );
    printf( "a+b     = %.20f\n", c     );
    printf( "(a+b)-a = %.20f\n", c - a );

    return 0;
}
