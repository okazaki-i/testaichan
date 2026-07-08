// gcc newton.c -lm && ./a.out
#include  <stdio.h>
#include  <stdlib.h>
#include  <math.h>

double newton( double x0, double threshold, int maxloop, double v ); //前方宣言
double f( double x, double v );
double df( double x, double v );

int main( void )
{
    double  x, v;
//    double  dv = 0.1/1000;
    double  dv = 0.5/1000;

//    v = 0.0/1000;
//    v = 40.0/1000;
    for ( v=0.0/1000; v<20.0/1000+dv/2; v+= dv ) {
        //x = newton( 0.0, 1e-12, 30+30, v ); //初期値、収束判定のしきい値、繰返し最大回数、滴定量v
        x = newton( 1.0, 1e-12, 30+30, v ); //初期値、収束判定のしきい値、繰返し最大回数、滴定量v
        printf( "v= %.4lf L : solution = %25.16le %6.3lf\n", v, x, -log10(x) );
    }
    return 0;
}

double newton( double x, double threshold, int maxloop, double v )
{
    int     i;
    double  dx;

//    printf( "#v=%.4lf\n", v );
//    printf( " %4d : %25.16le\n", 0, x );
    for ( i = 1; i < maxloop+1; i++ ) {
        dx = - f(x,v) / df(x,v);
        x = x + dx;
//        printf( " %4d : %25.16le  %25.16le\n", i, x, dx );
        if ( fabs( dx ) < threshold ) break;
    }
    if ( i == maxloop+1 ) {
        fprintf( stderr, " %4d : %25.16le  %25.16le    ", i, x, dx );
        fprintf( stderr, "not converged\n" );
        exit( 1 );
    }

    return x;
}

double f( double x, double v )
{
    double  v0=10.0/1000, m0=0.1, m=0.1, ka=1.74e-5, kw=1e-14;
    //return (v0+v)*x*x + ( (v0+v)*ka + m*v )*x + (m*v-m0*v0)*ka - (v0+v)*kw - (v0+v)*kw*ka/x; //解きづらいので使わない
    return (v0+v)*x*x*x + ( (v0+v)*ka + m*v )*x*x + ( (m*v-m0*v0)*ka - (v0+v)*kw )*x - (v0+v)*kw*ka;
}

double df( double x, double v )
{
    double  v0=10.0/1000, m0=0.1, m=0.1, ka=1.74e-5, kw=1e-14;
    //return 2.0*(v0+v)*x + ( (v0+v)*ka + m*v ) + (v0+v)*kw*ka/x/x; //解きづらいので使わない
    return 3.0*(v0+v)*x*x + 2.0*( (v0+v)*ka + m*v )*x + ( (m*v-m0*v0)*ka - (v0+v)*kw );
}

/* for gnuplot
v0=10.0/1000, m0=0.1, m=0.1, ka=1.74e-5, kw=1e-14;

f(x,v)= (v0+v)*x*x*x + ( (v0+v)*ka + m*v )*x*x + ( (m*v-m0*v0)*ka - (v0+v)*kw )*x - (v0+v)*kw*ka
finv(x,v)=(v0+v)*x*x + ( (v0+v)*ka + m*v )*x + (m*v-m0*v0)*ka - (v0+v)*kw - (v0+v)*kw*ka/x

plot for [v in "0 5 10 15 20"] f(x,v/1000.0) title sprintf("v=%s",v)
plot for [v in "0 5 10 15 20"] finv(x,v/1000.0) title sprintf("v=%s",v)
*/
