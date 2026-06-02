#!/usr/bin/env python3
# metropolis_states.py
#
# 状態数: NSTATES
#   A00 : E = 0.0
#   A01 : E = 0.1
#   A02 : E = 0.2
#    ...
#   Axx : E = xxx
#
# メトロポリス法で状態遷移を行い、
# 各状態やエネルギーの出現頻度を数える。
#
# 2026/05/28 coded by chargpt
# 2026/06/03 modified by okazaki,i

import random
import math
from collections import Counter

# 状態とエネルギー
NSTATES = 10
states = [ "A" + f"{i:02d}" for i in range(NSTATES) ]
energy = { s : 0.1 * i for i, s in enumerate(states) }  #ΔE

# 温度パラメータ, beta = 1/(k_B T), ここでは k_B = 1 とする
beta = 1.0

# シミュレーション回数
#n_steps = 10000000
n_steps = 100000
#n_steps =  10

# 初期状態
current = states[0]

# 記録用
state_count = Counter()
energy_count = Counter()

# ----------------------------
# メトロポリス法
for step in range( n_steps ):

    # 候補状態をランダムに選ぶ
    proposal = random.choice( states )

    # エネルギー差
    dE = energy[proposal] - energy[current]

    # 受理判定
    if dE <= 0:
        accept = True
    else:
        r = random.random()
        if r < math.exp( -beta * dE ):
            accept = True
        else:
            accept = False

    # 状態更新
    if accept:
        current = proposal

    # 統計を取る
    state_count[current] += 1
    energy_count[energy[current]] += 1

# ----------------------------
# 結果表示
print( "=== state (energy): probability ===")
for s in states:
    p = state_count[s] / n_steps
    print( f"{s} ( {energy[s]:.3f} ): {p:.5f}" )

print( "=== energy probability ===" )
for E in sorted( energy_count.keys() ):
    p = energy_count[E] / n_steps
    print( f"E={E:.3f}: {p:.5f}" )

# ----------------------------
# 理論値
weights = { s: math.exp( -beta * energy[s] ) for s in states }
Z = sum( weights.values() )
state_prob = { s: weights[s] / Z for s in states }
energy_prob = Counter()
for s in states:
    energy_prob[ energy[s] ] += state_prob[s]  #縮退があれば加算

print("=== theoretical ===")
for s in states:
    print( f"{s} ( {energy[s]:.3f} ): {state_prob[s]:.5f}" )
print("=== Energy theoretical ===")
for E in sorted(energy_prob.keys()):
    print( f"E={E:.3f}: {energy_prob[E]:.5f}" )

# end of file
