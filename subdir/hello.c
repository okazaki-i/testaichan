// 2026-05-24
#include <stdio.h>
#include <time.h>

int main(void)
{
    time_t now;
    struct tm *tm_now;
    char date[11];

    printf("Hello world\n");
    now = time(NULL);
    tm_now = localtime(&now);
    if (tm_now != NULL && strftime(date, sizeof(date), "%Y-%m-%d", tm_now) > 0) {
        printf("%s\n", date);
    } else {
        printf("none\n");
    }
    return 0;
}
