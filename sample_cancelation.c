#include  <stdio.h>
#include  <math.h>

int main( void )
{
    double x = 1.0e+8;

    double  y1 = sqrt( x + 1.0 ) - sqrt( x );
    double  y2 = 1.0 / ( sqrt( x + 1.0 ) + sqrt( x ) );

    printf( "direct     = %.20e\n", y1 );
    printf( "transformed= %.20e\n", y2 );

    return 0;
}
