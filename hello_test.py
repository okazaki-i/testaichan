#!/usr/bin/env python3
"""簡単なテスト用スクリプト。"""


def add(a: float, b: float) -> float:
    """2つの実数の合計を返す。"""
    return a + b


if __name__ == "__main__":
    x, y = 2.5, 3.1
    print(f"{x} + {y} = {add(x, y)}")
