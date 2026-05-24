// 2026-05-24
#include <stdio.h>
#include <time.h>

int main(void)
{
    time_t now;
    struct tm *tm_now;
    char datetime[20];

    printf("Hello world\n");
    now = time(NULL);
    tm_now = localtime(&now);
    if (tm_now != NULL && strftime(datetime, sizeof(datetime), "%Y-%m-%d %H:%M:%S", tm_now) > 0) {
        printf("%s\n", datetime);
    } else {
        printf("none\n");
    }
    return 0;
}
