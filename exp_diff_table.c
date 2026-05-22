/*
  exp(x)の微分値の近似 ( exp(x+h) - exp(x-h) ) / (2*h) と
  正しい値 exp(x) の比較


？？？
  h が小さすぎると丸め誤差が目立ち、
  h が大きすぎると離散化誤差が目立つ区間を比較しやすいように設定。

  $ gcc exp_diff_table.c -lm && ./a.out
  $ ./a.out
  $ gnuplot
  gnuplot> splot '< ./a.out' u 1:2:5 w l, 1e-16  #対数軸がにするとよい
*/

#include  <math.h>
#include  <stdio.h>

int main( void )
{
    double  x_values[] = {
        -40.0, -35.0, -30.0, -25.0, -20.0, -15.0, -10,0, -5.0,  0.0,
          5.0,  10.0,  15.0,  20.0,  25.0,  30.0,  35.0, 40.0
    };
    double  h_values[] = { 1e-16, 1e-12, 1e-8, 1e-4, 1e-1, 1.0 };

    int  x_count = (int)( sizeof(x_values) / sizeof(x_values[0]) );
    int  h_count = (int)( sizeof(h_values) / sizeof(h_values[0]) );

    printf( "#%11s %12s %22s %22s %22s\n",
            "x", "h", "exp(x)",
            "diff_approx", "|relative error|" );
    printf( "#%11s %12s %22s %22s %22s\n",
            "-----------", "------------", "----------------------",
            "----------------------", "----------------------" );

    for ( int i = 0; i < x_count; i++ ) {
        double x     = x_values[i];
        double exact = exp(x);  // d/dx exp(x) = exp(x)

        for ( int j = 0; j < h_count; j++ ) {
            double  h      = h_values[j];
            double  approx = ( exp(x+h) - exp(x-h) ) / (2.0*h);
            double  err    = fabs( (approx - exact) / exact );

            printf( "%12.4f %12.1e %22.14e %22.14e %22.14e\n",
                    x, h, exact, approx, err );
        }
        printf( "\n" );
    }

    return 0;
}
