"""簡単なテスト用スクリプト。"""


def add(a: int, b: int) -> int:
    """2つの整数の合計を返す。"""
    return a + b


if __name__ == "__main__":
    x, y = 2, 3
    print(f"{x} + {y} = {add(x, y)}")
