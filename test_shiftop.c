#include  <stdio.h>

int main( void )
{
//    double d = 12.3;
    int d = 12.3;

    if ( d>>1 ) {  //右シフト演算子の仕様確認
        printf( "T\n" );
    } else {
        printf( "F\n" );
    }

    return 0;
}
