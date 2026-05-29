#include <stdio.h>
#include <string.h>

static const char *find_environment_value(char *envp[], const char *name)
{
    size_t name_length;
    int i;

    name_length = strlen(name);
    for (i = 0; envp[i] != NULL; i++) {
        if (strncmp(envp[i], name, name_length) == 0
            && envp[i][name_length] == '=') {
            return envp[i] + name_length + 1;
        }
    }

    return NULL;
}

static int uses_japanese(char *envp[])
{
    const char *value;

    value = find_environment_value(envp, "LANG");
    return value != NULL && (value[0] == 'j' || value[0] == 'J')
        && (value[1] == 'a' || value[1] == 'A');
}

static void print_error(char *envp[], const char *english, const char *japanese)
{
    if (uses_japanese(envp)) {
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

int main(int argc, char *argv[], char *envp[])
{
    long long dividend;
    long long divisor;

    if (argc != 3) {
        print_error(
            envp,
            "Usage: divisible POSITIVE_INTEGER POSITIVE_INTEGER",
            "使い方: divisible 正の整数 正の整数");
        return -1;
    }

    if (parse_positive_integer(argv[1], &dividend) != 0
        || parse_positive_integer(argv[2], &divisor) != 0) {
        print_error(
            envp,
            "Error: arguments must be positive integers.",
            "エラー: 引数は正の整数でなければなりません。");
        return -1;
    }

    if (dividend % divisor == 0) {
        return 0;
    }

    return 1;
}
