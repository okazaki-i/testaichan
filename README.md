# testaichan

このリポジトリは、標準出力の状態判定、文字列切り出し、ビット配列表示、指数差分テーブル生成などの挙動を試すための小さな実験用コードをまとめたものです。

## ファイル一覧（全ファイル）

以下は、`git ls-files` で確認できる全ファイルです。

### ルートディレクトリ

- `.editorconfig`  
  エディタ設定（インデントなど）の共通ルールです。

- `.gitignore`  
  Gitで追跡しないファイルの設定です。

- `AGENTS.md`  
  このリポジトリで作業するエージェント向けの作業方針・制約です。

- `README.md`  
  このリポジトリの概要と各ファイル説明です。

- `mycut`  
  Python製の簡易 cut 風コマンドです。標準入力を1行ずつ読み取り、デフォルトで先頭100文字（`-c/--characters` で変更可能）を出力します。ANSIカラーコードを考慮して文字数を数える実装になっています。

- `hello_test.py`  
  `mycut` の基本挙動を確認する pytest テストです。

- `test_mycut.py`  
  `mycut` の別観点の挙動確認用 pytest テストです。

- `outswtch.c`  
  stdout が端末・パイプ・通常ファイルのどれに接続されているかを判定して表示する C プログラムです。

- `sample_cancelation.c`  
  浮動小数点演算での桁落ち（cancelation）の挙動を確認するサンプルです。

- `sample_infoloss.c`  
  浮動小数点演算における情報落ち（infoloss）の挙動を確認するサンプルです。

- `exp_diff_table.c`  
  指数関数差分に関するテーブルを生成する C コードです。

- `exp_diff_table.png`  
  `exp_diff_table.c` の出力例画像です。

- `bit_array_display.c`  
  ビット列や配列の表示確認を目的とした C サンプルです。

- `bit_array_display-intx.c`  
  `bit_array_display` 系の整数表示系バリエーションです。

- `bit_array_display-ans.c`  
  `bit_array_display` 系の比較・参照用バリエーションです。

- `test.c`  
  C 言語の小さな動作確認用サンプルです。

### subdir/

- `subdir/.gitignore`  
  `subdir/` 配下の Git 除外設定です。

- `subdir/.gitkeep`  
  ディレクトリ維持のためのプレースホルダファイルです。

- `subdir/hello.c`  
  C 言語のサンプルです。

- `subdir/hello.cpp`  
  C++ 言語のサンプルです。

- `subdir/hello.py`  
  Python 言語のサンプルです。

- `subdir/hello.f90`  
  Fortran 言語のサンプルです。

- `subdir/hello.bas`  
  BASIC 言語のサンプルです。

- `subdir/hello.pas`  
  Pascal 言語のサンプルです。

- `subdir/mycut`  
  `subdir/` 配下に置かれた `mycut` 関連の補助スクリプトです。

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

### Cプログラム例（outswtch.c）

```bash
gcc outswtch.c -o outswtch
./outswtch
./outswtch | cat
./outswtch > out.txt
```

## 補足

- `mycut` の `--color` は `auto` / `never` / `always` を受け付けます。
- このリポジトリは学習・検証用途の小規模サンプルです。
