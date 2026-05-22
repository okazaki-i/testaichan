#include <stdio.h>
#include <stdint.h>

int main(void) {
    int i = 123;
    int int_bits = (int)(sizeof(int) * 8);

    printf("i = %d\n", i);
    printf("int bit array: ");
    for (int b = int_bits - 1; b >= 0; b--) {
        putchar(((i >> b) & 1) ? '1' : '0');
        if (b % 8 == 0 && b != 0) {
            putchar(' ');
        }
    }
    putchar('\n');

    double d = 12.3;
    union {
        double d;
        uint64_t u;
    } d_bits;
    d_bits.d = d;

    printf("d = %.1f\n", d);
    printf("double bit array: ");
    for (int b = (int)(sizeof(d_bits.u) * 8) - 1; b >= 0; b--) {
        putchar(((d_bits.u >> b) & 1ULL) ? '1' : '0');
        if (b % 8 == 0 && b != 0) {
            putchar(' ');
        }
    }
    putchar('\n');

    return 0;
}
