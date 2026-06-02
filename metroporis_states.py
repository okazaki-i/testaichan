#!/usr/bin/env python3
# 2026/05/28 coded by chargpt
#
# metropolis_states.py
#
# 状態:
#   A : E = 0
#   B : E = 1
#   C : E = 1
#
# メトロポリス法で状態遷移を行い、
# 各状態やエネルギーの出現頻度を数える。

import random
import math
from collections import Counter

# ----------------------------
# 状態とエネルギー
# ----------------------------
states = ["A", "B", "C"]

energy = {
    "A": 0.0,
    "B": 1.0,
    "C": 1.0,
}

# ----------------------------
# 温度パラメータ
# beta = 1/(k_B T)
# ここでは k_B = 1 とする
# ----------------------------
beta = 1.0

# ----------------------------
# シミュレーション回数
# ----------------------------
n_steps = 100000

# ----------------------------
# 初期状態
# ----------------------------
current = "A"

# 記録用
state_count = Counter()
energy_count = Counter()

# ----------------------------
# メトロポリス法
# ----------------------------
for step in range(n_steps):

    # 候補状態をランダムに選ぶ
    proposal = random.choice(states)

    # エネルギー差
    dE = energy[proposal] - energy[current]

    # 受理判定
    accept = False

    if dE <= 0:
        accept = True
    else:
        r = random.random()

        if r < math.exp(-beta * dE):
            accept = True

    # 状態更新
    if accept:
        current = proposal

    # 統計を取る
    state_count[current] += 1
    energy_count[energy[current]] += 1

# ----------------------------
# 結果表示
# ----------------------------
print("=== state probability ===")

for s in states:
    p = state_count[s] / n_steps
    print(f"{s}: {p:.5f}")

print()

print("=== energy probability ===")

for E in sorted(energy_count.keys()):
    p = energy_count[E] / n_steps
    print(f"E={E}: {p:.5f}")

# ----------------------------
# 理論値
# ----------------------------
Z = (
    math.exp(-beta * 0)
    + math.exp(-beta * 1)
    + math.exp(-beta * 1)
)

pA = math.exp(0) / Z
pB = math.exp(-beta) / Z
pC = math.exp(-beta) / Z

print()
print("=== theoretical ===")
print(f"A: {pA:.5f}")
print(f"B: {pB:.5f}")
print(f"C: {pC:.5f}")

print()
print("Energy theoretical:")
print(f"E=0: {pA:.5f}")
print(f"E=1: {pB + pC:.5f}")
