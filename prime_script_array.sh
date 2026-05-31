#!/usr/bin/env bash

max=${max:-100}

for (( i = 2; i <= max; i++ )); do
    number[i]=1

    for (( j = 2; j < i; j++ )); do
        if (( i % j == 0 )); then
            number[i]=0
            break
        fi
    done
done

for (( i = 2; i <= max; i++ )); do
    echo $i ${number[i]}
done
