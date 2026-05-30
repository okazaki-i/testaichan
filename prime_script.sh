#!/usr/bin/env bash

max=${max:-100}

for (( i = 2; i <= max; i++ )); do
    is_prime=1

    for (( j = 2; j < i; j++ )); do
        if (( i % j == 0 )); then
            is_prime=0
            break
        fi
    done

#    if (( is_prime != 0 )); then  #これでもよい
    if [ $is_prime -ne 0 ]; then
        echo $i
    fi
done
