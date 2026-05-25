# testaichan

このリポジトリは、Codexを試しつつ作った、次のような小さなコードを含む。
標準出力の状態判定、数値のビット配列表示、数値計算を考えるコード。

## ファイル一覧

### ルートディレクトリ

- `.editorconfig`
  エディタ設定（インデントなど）の共通ルール。VScodeなどが使うらしい。

- `AGENTS.md`
  このリポジトリで作業するエージェント向けの作業方針・制約

- `README.md`
  このリポジトリの概要と説明


- `outswtch.c`
  stdout が端末・パイプ・通常ファイルのどれに接続されているかを判定して、その結果を表示するテストプログラムです。

- `mycut`
  Python製の簡易 cut 風コマンド。
標準入力を1行ずつ読み取り、デフォルトで先頭100文字（`-c/--characters` で変更可能）を出力します。
ANSIカラーコードを考慮して文字数を数える実装になっています。日本語文字も対応。
出力先の種類に応じてカラーを取り除いたりもします。

- `test_mycut.py`
  `mycut` の挙動確認用 pytest テストです。


- `bit_array_display.c`
  intとdoubleのビット列の表示確認を目的としたプログラムです。
`bit_array_display-ans.c` はいくつかのコード追加してコメントアウトしたバージョンである。
`bit_array_display-endi.c` はintについて、エンディアン確認を目的としたプログラムである。

- `sample_infoloss.c`
  浮動小数点演算における情報落ち（infoloss）の挙動を確認するサンプルです。

- `sample_cancelation.c`
  浮動小数点演算での桁落ち（cancelation）の挙動を確認するサンプルです。

- `exp_diff_table.c`
  指数関数差分に関するテーブルを生成する C コードです。
`exp_diff_table.png` は出力データを画像にしたものである。


- `test_shiftop.c`
  C 言語の右シフト演算子の仕様確認のためのテストコードです。


- `hello_test.py`
  `mycut` の基本挙動を確認する pytest テストです。


### subdir/

- hello.c, hello.cpp, hello.py, hello.f90, hello.bas, hello.pas
  それぞれ順に C, C++, Python, Fortran, BASIC, Pascal 言語のサンプルプログラムです。

- mycut
  Codexで作った四則演算をするプログラムです。


## 使い方

### mycut

```bash
chmod +x mycut
printf 'abcdefghijklmnopqrstuvwxyz\n' | ./mycut
printf 'abcdefghijklmnopqrstuvwxyz\n' | ./mycut -c 5
printf '\033[31mred\033[0m text\n' | ./mycut --color=always
```


### テスト実行

```bash
pytest -q
```
これは未確認


### Cプログラム例（outswtch.c）

```bash
gcc outswtch.c
./a.out
./a.out | cat
./a.out > out.txt
```


## 補足

- `mycut` の `--color` は `auto` / `never` / `always` を受け付けます。
