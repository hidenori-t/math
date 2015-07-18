#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
[関数の可視化](http://qiita.com/richi40/items/d7c862dec06368a212cb)
機械学習の動きを確認したいが、numpy、scipy、pandas、matplotlibに慣れていないので、シミュレーションデータを作成できず、歯がゆいことが多いのでまとめる。
"""

# インポート
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
row = 3; col = 2

# 1次関数
func = lambda x, a, b : a*x + b
ax01 = fig.add_subplot(row, col, 1)
x = np.linspace(-3, 3, 100)
a = 10; b = 5
ax01.plot(
    x,
    func(x, a, b)
)
ax01.set_title('$f(x) = 10x + 5$')

# 2次関数
func = lambda x, a, b, c : a*pow(x,2) + b*x + c
ax02 = fig.add_subplot(row, col, 2)
a = 1; b = 1; c = 1
ax02.plot(
    x,
    func(x, a, b, c)
)
ax02.set_title('$f(x) = x^2 + x + 1$')

# 3次関数
func = lambda x, a, b, c, d : a*pow(x,3) + b*pow(x,2) + c*x + d
ax03 = fig.add_subplot(row, col, 3)
a = 1; b = 1; c = 1; d = 1
ax03.plot(
    x,
    func(x, a, b, c, d)
)
ax03.set_title('$f(x) = x^3 + x^2 + x + 1$')

# 指数関数
func = lambda x : np.exp(x)
ax04 = fig.add_subplot(row, col, 4)
ax04.plot(
    x,
    func(x)
)
ax04.set_title('$f(x) = exp(x)$')

# 対数関数
func = lambda x : np.log(x)
ax05 = fig.add_subplot(row, col, 5)
ax05.plot(
    x,
    func(x)
)
ax05.set_title('$f(x) = log(x)$')

# 描画
fig.tight_layout()
plt.show()
