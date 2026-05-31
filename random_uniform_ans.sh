#!/usr/bin/bash

#たとえば
#  for i in `seq 1 20` ; do ./random.sh; done
#で20個の区間[0,1)の一様乱数が得られる。

#1000個くらいを出力をファイル(output.txt)に保存し、
#  awk 'BEGIN{ bin=0.1 } { f[ int($1/bin) ]++ } END{ for( i in f ) print i*bin, f[i] }' output.txt
#でヒストグラムを見てみるとよい。

intmax=2147483647             #符号付き４バイト整数の最大値
intmin=$(( -intmax - 1 ))     #          〃          最小値

#右辺のコマンド:
#ファイル/dev/urandomからランダムなビット列を４バイト得て(-N4)、
#符号付き４バイト整数として表示する(-td4)、ただしアドレスは出力しない(-An)
v=`od  -An -N4 -td4 /dev/urandom`

#bcコマンドで計算し [0,1)区間の値に変換する。なお 16桁表示する(scale=16)
echo "scale=16; ( $v / ( - $intmin ) + 1.0 ) / 2.0" | bc


exit
memo:

cd random_uniform.sh.out

#1/2*exp(-x/2)の指数分布（確率密度分布）を一様乱数から作成
for i in `seq 1 1000` ; do ../random_uniform.sh; done | tee  random_uniform.sh.out-1000
awk '{print -2 * log( 1 - $1 ) }' random_uniform.sh.out-1000 > random_uniform.sh.out-1000-fexp

#ヒストグラム作成
awk 'BEGIN{ bin=0.1 } { f[ int($1/bin) ]++ } END{ for( i in f ) print i*bin, f[i] }' \
     random_uniform.sh.out-1000-fexp > random_uniform.sh.out-1000-fexp-hist

#ヒストグラムを各区間に入る確率 count/N を求め、確率密度を区間幅を掛けて確率にして、比較
plot 'random_uniform.sh.out-1000-fexp-hist' u ($1+0.1/2):($2/1000) w i, 1.0/2*exp(-x/2)*0.1 w lp

