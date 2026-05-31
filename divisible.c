/*
  $ gcc divisible.c -o divisible
  $ ./divisible 10 2  ; echo $?
  $ ./divisible 10 3  ; echo $?
  $ ./divisible 10 3a ; echo $?
  直前のコマンドの終了ステータスを $? で知ることができます。

  $ LANG=en_US.UTF-8 ./divisible 10 3a
  $ LANG=ja_JP.UTF-8 ./divisible 10 3a
  ロケール (LANGに代入している値) のフォーマットは "言語_国.文字コード" であり、
  言語や地域に応じた表示 (言語と、年月日、通貨や小数点記号など）を指定するもの
  である。
*/

#include <stdio.h>
#include <stdlib.h>  //getenvのため
#include <string.h>  //strcmpのため

void print_error( char *english, char *japanese )
{
    char*  v = getenv( "LANG" );  //環境変数LANGの値を得る
    if ( v != NULL
         && ( v[0] == 'j' || v[0] == 'J' )
         && ( v[1] == 'a' || v[1] == 'A' ) ) {
        fprintf( stderr, "%s\n", japanese ); //値がjaで始まっているとき
    } else {
        fprintf( stderr, "%s\n", english  ); //それ以外
    }
    return;
}

int parse_positive_integer( char *text, long long *value )
{
    char  value2text[256];
    if ( sscanf( text, "%lld", value ) != 1 ) {
        //数字でなかった
        fprintf( stderr, "scan failed: text=[%s]\n", text );
        return -1;
    }
    if ( *value <= 0 ) {
        //正でなかった
        fprintf( stderr, "not positive: text=[%s]\n", text );
        return -1;
    }
    sprintf( value2text, "%lld", *value );
    if ( strcmp( text, value2text ) != 0 ) {
        //123abc, 00123, +123 のような値は sscanfで123と読まれるが、エラーにする
        //オーバーフローのときもここでエラーになる
        fprintf( stderr, "not matched: text=[%s], value2text=[%s]\n", text, value2text );
        return -1;
    }
    return 0;
}

int main( int argc, char *argv[] )
{
    long long  dividend, divisor;

    if ( argc != 2+1 ) {
        print_error( "Usage: divisible POSITIVE_INTEGER POSITIVE_INTEGER",
                     "使い方: divisible 正の整数 正の整数" );
        return 255;
    }

    if (    parse_positive_integer( argv[1], &dividend ) != 0
         || parse_positive_integer( argv[2], &divisor  ) != 0 ) {
        print_error( "Error: arguments must be positive integers.",
                     "エラー: 引数は正の整数でなければなりません。");
        return 255;
    }

    if ( dividend % divisor == 0 ) {
        return 0;
    } else {
        return 1;
    }
}
