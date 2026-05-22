# testaichan

このリポジトリは、標準出力の状態判定、文字列切り出し、ビット配列表示、指数差分テーブル生成などの挙動を試すための小さな実験用コードをまとめたものです。

## 構成

- mycut  
  Python製の簡易 cut 風コマンドです。標準入力を1行ずつ読み取り、デフォルトで先頭100文字（-c/--characters で変更可能）
  を出力します。ANSIカラーコードを考慮して文字数を数える実装になっています。

- test_mycut.py  
  mycut の基本挙動（改行あり/なし入力時の出力）を確認する pytest テストです。

- outswtch.c  
  stdout が端末・パイプ・通常ファイルのどれに接続されているかを判定して表示するCプログラムです。

- sample_cancelation.c  
  浮動小数点演算での桁落ち（cancelation）の挙動を確認するためのサンプルです。

- exp_diff_table.c / exp_diff_table.png  
  指数関数差分に関するテーブル生成コードと、その出力例画像です。

- bit_array_display.c  
  ビット列や配列の表示確認を目的としたCサンプルです。

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

- mycut の --color は auto/never/always を受け付けます。
- このリポジトリは学習・検証用途の小規模サンプルです。
