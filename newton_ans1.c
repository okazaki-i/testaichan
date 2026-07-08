// gcc newton.c -lm && ./a.out
#include  <stdio.h>
#include  <stdlib.h>
#include  <math.h>

double newton( double x0, double threshold, int maxloop ); //前方宣言
double f( double x );
double df( double x );

int main( void )
{
    double  x0, x;

//    x0 = 1.0;
//    x0 = -1.0;
    x0 = -4.0;
    x = newton( x0, 1e-12, 30+10 ); //初期値、収束判定のしきい値、繰返し最大回数
    printf( "#solution= %.15f\n", x );
    return 0;
}

double newton( double x, double threshold, int maxloop )
{
    int     i;
    double  dx;

    printf( " %4d : %25.16le\n", 0, x );
    for ( i = 1; i < maxloop+1; i++ ) {
        dx = - f(x) / df(x);
        x = x + dx;
        printf( " %4d : %25.16le  %25.16le\n", i, x, dx );
        if ( fabs( dx ) < threshold ) break;
    }
    if ( i == maxloop+1 ) {
        fprintf( stderr, "not converged\n" );
        exit( 1 );
    }

    return x;
}

double f( double x )
{
//    return x*x-2.0;
//    return exp(-x)-x;
//    return cos(x)-x;
    return cos(x)-x/5.0;
}

double df( double x )
{
//    return 2.0*x;
//    return -exp(x)-1.0;
//    return -sin(x)-1.0;
    return -sin(x)-1.0/5.0;
}
