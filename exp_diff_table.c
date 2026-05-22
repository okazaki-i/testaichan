#include <math.h>
#include <stdio.h>

int main(void) {
    /*
     * exp(x) の中心差分近似:
     * (exp(x+h) - exp(x-h)) / (2*h)
     *
     * h が小さすぎると丸め誤差が目立ち、
     * h が大きすぎると離散化誤差が目立つ区間を比較しやすいように設定。
     */
    const double x_values[] = {-40.0, -20.0, -5.0, 0.0, 5.0, 20.0, 40.0};
    const double h_values[] = {1e-16, 1e-12, 1e-8, 1e-4, 1e-1, 1.0};

    const int x_count = (int)(sizeof(x_values) / sizeof(x_values[0]));
    const int h_count = (int)(sizeof(h_values) / sizeof(h_values[0]));

    for (int j = 0; j < h_count; j++) {
        const double h = h_values[j];

        if (j > 0) {
            putchar('\n');
        }

        printf("# h = %.1e\n", h);
        printf("#%12s %22s %22s %22s\n",
               "x", "exp(x)", "diff_approx", "|error|");
        printf("#%12s %22s %22s %22s\n",
               "------------", "----------------------",
               "----------------------", "----------------------");

        for (int i = 0; i < x_count; i++) {
            const double x = x_values[i];
            const double exact = exp(x); /* d/dx exp(x) = exp(x) */
            const double approx = (exp(x + h) - exp(x - h)) / (2.0 * h);
            const double err = fabs(approx - exact);

            printf("%13.4f %22.14e %22.14e %22.14e\n",
                   x, exact, approx, err);
        }
    }

    return 0;
}
