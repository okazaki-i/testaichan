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

    x0 = 1.0; //-> -0.5
//    x0 = 2.0; //->  1.5
//    x0 = 0.1; //->  0.5

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
//    return x*x-2.0;
//    return 8.0*( x*x*x-3.0/2.0*x*x-1.0/4.0*x+3.0/8.0 );  // (2*x-1)*(2*x-3)*(2*x+1)
//    return x*x+2.0;
    return x*x;
}

double df( double x )
{
//    return 2.0*x;
//    return 8.0*( 3.0*x*x-3.0*x-1.0/4.0 );
//    return 2.0*x;
    return 2.0*x;
}
