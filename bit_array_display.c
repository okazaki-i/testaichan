#include  <stdio.h>
#include  <stdint.h>  //unit64_tを使うため
//#include  <math.h>

int main( void )
{
    int  i = 123;
    int  int_bits = (int)( sizeof(int) * 8 );  //多くの場合８バイト

    printf( "i = %d\n", i );
    printf( "int bit array: " );
    for ( int b = int_bits - 1; b >= 0; b-- ) {
        putchar( ( (i >> b) & 1 ) ? '1' : '0' );  //bビット目の値
        if ( b % 8 == 0 && b != 0 ) putchar( ' ' );
    }
    putchar( '\n' );

    double d = 12.3;
//    d = d / 0.0;
//    d = log( -d );
//    double d = 1.0/3.0;
    union {
        double    d;
        uint64_t  u;  //doubleが８バイトを仮定
    } d_bits;
    d_bits.d = d;

    printf( "d = %.1lf\n", d );
//    printf( "d = %.50lf\n", d );
    printf( "double bit array: " );
    for ( int b = (int)( sizeof(d_bits.u) * 8 ) - 1; b >= 0; b--) {
        putchar( ( (d_bits.u >> b) & 1 ) ? '1' : '0' ); //>>は整数型のみ可
        if (b % 8 == 0 && b != 0 ) putchar(' ');
    }
    putchar('\n');

    return 0;
}
