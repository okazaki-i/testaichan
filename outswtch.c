/*
出力先の種類を知るサンプルコード

$ gcc outswtch.c
  $ ./a.out
stdout = terminal
  $ ./a.out | cat
stdout = pipe
  $ ./a.out > temp.out; cat temp.out
stdout = regular file
  $ ./a.out |less
stdout = pipe

  2026/05/20 coded by codex
*/


#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main(void)
{
    struct stat st;

    if (isatty(STDOUT_FILENO)) {
        printf("stdout = terminal\n");
        return 0;
    }

    if (fstat(STDOUT_FILENO, &st) == -1) {
        perror("fstat");
        return 1;
    }

    if (S_ISFIFO(st.st_mode)) {
        printf("stdout = pipe\n");
    }
    else if (S_ISREG(st.st_mode)) {
        printf("stdout = regular file\n");
    }
    else {
        printf("stdout = other\n");
    }

    return 0;
}
