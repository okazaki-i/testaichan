#!/usr/bin/env python3
# 2026/05/28 coded by chargpt
#
# metropolis_states.py
#
# 状態:
#   A : E = 0
#   B-J : E = 1
#
# メトロポリス法で状態遷移を行い、
# 各状態やエネルギーの出現頻度を数える。

import random
import math
from collections import Counter

# ----------------------------
# 状態とエネルギー
# ----------------------------
states = [chr(ord("A") + i) for i in range(10)]

energy = {s: 1.0 for s in states}
energy["A"] = 0.0

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
weights = {s: math.exp(-beta * energy[s]) for s in states}
Z = sum(weights.values())

state_prob = {s: weights[s] / Z for s in states}
energy_prob = Counter()

for s in states:
    energy_prob[energy[s]] += state_prob[s]

print()
print("=== theoretical ===")

for s in states:
    print(f"{s}: {state_prob[s]:.5f}")

print()
print("Energy theoretical:")

for E in sorted(energy_prob.keys()):
    print(f"E={E}: {energy_prob[E]:.5f}")
