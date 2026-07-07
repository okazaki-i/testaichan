// gcc newto.c -lm && ./a.out
#include  <stdio.h>
#include  <stdlib.h>
#include  <math.h>

double newton( double x );
double f( double x );
double df( double x );

int main( void )
{
    double  x0, x;

    x0 = 1.0;

    x = newton( x0 );
    printf( "solution = %.15f\n", x );

    return 0;
}

double newton( double x )
{
    int     i;
    double  xnew, dx;

    for ( i = 1; i <= 30; i++ ) {

        dx = - f(x) / df(x);
        x = x + dx;

        printf( "%2d : %.15lf  %.15lf\n", i, x, dx );

        if ( fabs( dx ) < 1e-12 ) break;
    }

    return x;
}

double f( double x )
{
    return x*x-2.0;
}

double df( double x )
{
    return 2.0*x;
}
