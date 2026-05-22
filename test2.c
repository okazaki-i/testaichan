#include  <stdio.h>
#include  <stdint.h>

int main( void )
{
    double d = -12.3;
    union {
        double    d;
        uint64_t  u;
    } d_bits;

    d_bits.d = d;
    uint64_t shifted = d_bits.u >> 1;

    if ( shifted ) {
        printf( "True\n" );
    } else {
        printf( "False\n" );
    }

    return 0;
}
