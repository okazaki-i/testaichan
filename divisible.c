#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int uses_japanese(void)
{
    const char *value;

    value = getenv("LANG");
    return value != NULL && (value[0] == 'j' || value[0] == 'J')
        && (value[1] == 'a' || value[1] == 'A');
}

static void print_error(const char *english, const char *japanese)
{
    if (uses_japanese()) {
        fprintf(stderr, "%s\n", japanese);
    } else {
        fprintf(stderr, "%s\n", english);
    }
}

static int parse_positive_integer(const char *text, long long *value)
{
    char extra;
    char formatted[32];
    long long parsed;

    if (sscanf(text, "%lld%c", &parsed, &extra) != 1 || parsed <= 0) {
        return -1;
    }

    sprintf(formatted, "%lld", parsed);
    if (strcmp(text, formatted) != 0) {
        return -1;
    }

    *value = parsed;
    return 0;
}

int main(int argc, char *argv[])
{
    long long dividend;
    long long divisor;

    if (argc != 3) {
        print_error(
            "Usage: divisible POSITIVE_INTEGER POSITIVE_INTEGER",
            "使い方: divisible 正の整数 正の整数");
        return -1;
    }

    if (parse_positive_integer(argv[1], &dividend) != 0
        || parse_positive_integer(argv[2], &divisor) != 0) {
        print_error(
            "Error: arguments must be positive integers.",
            "エラー: 引数は正の整数でなければなりません。");
        return -1;
    }

    if (dividend % divisor == 0) {
        return 0;
    }

    return 1;
}
