#!/usr/bin/env bash

max=${max:-100}

prime_count=1
for (( i = 2; i <= max; i++ )); do
    is_prime=1

    for (( j = 2; j < i; j++ )); do
        ./divisable $i $j
        if [ $? -eq 0 ]; then
            is_prime=0
            break
        fi
    done

#    if (( is_prime != 0 )); then  #これでもよい
    if [ $is_prime -ne 0 ]; then
        echo $prime_count $i   #gnuplot> plot 'prime_script_stream_ans.sh.out' u 2:1 w steps
        (( prime_count++ ))    #         , x/log(x)*1.15 w l
    fi
done
