/*
 $ gcc bit_array_display-intx.c -lm && ./a.out
*/
#include  <stdio.h>

int main( void )
{
    int  i = 123;
    int  int_bits = (int)( sizeof(int) * 8 );  //多くの場合８バイト

    printf( "i = %d\n", i );
    printf( "i = 0x%X\n", i );

    printf( "int bit array: " );
    for ( int b = int_bits - 1; b >= 0; b-- ) {
        putchar( ( (i >> b) & 1 ) ? '1' : '0' );  //bビット目の値
        if ( b % 8 == 0 && b != 0 ) putchar( ' ' );
    }
    putchar( '\n' );

    return 0;
}
