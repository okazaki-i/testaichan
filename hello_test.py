#!/usr/bin/env python3
"""簡単なテスト用スクリプト。"""

def add(a: float, b: float) -> float:
    """2つの実数の合計を返す。"""
    return a + b

def subtract(a: float, b: float) -> float:
    """2つの実数の差を返す。"""
    return a - b

def multiply(a: float, b: float) -> float:
    """2つの実数の積を返す。"""
    return a * b

def divide(a: float, b: float) -> float:
    """2つの実数の商を返す。"""
    if b == 0:
        raise ValueError("0で割ることはできません。")
    return a / b

def subtract(a: float, b: float) -> float:
    """2つの実数の差を返す。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの実数の積を返す。"""
    return a * b


def divide(a: float, b: float) -> float:
    """2つの実数の商を返す。"""
    if b == 0:
        raise ValueError("0で割ることはできません。")
    return a / b


def divrem(a: int, b: int) -> tuple[int, int]:
    """2つの整数を割ったときの商と余りを返す。"""
    if b == 0:
        raise ValueError("0で割ることはできません。")
    return divmod(a, b)


if __name__ == "__main__":
    x, y = 2.5, 3.1
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")

    m, n = 17, 5
    q, r = divrem(m, n)
    print(f"{m} ÷ {n} = 商 {q}, 余り {r}")
