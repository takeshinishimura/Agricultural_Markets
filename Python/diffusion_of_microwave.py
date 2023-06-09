#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# !pip install japanize-matplotlib
# !pip install matplotx

import numpy as np
import pandas as pd
import math
import japanize_matplotlib
import matplotx
from matplotlib import pyplot as plt

df = pd.read_excel("https://www.esri.cao.go.jp/jp/stat/shouhi/0403fukyuritsu.xls", header=2, skipfooter=2)

df = df.replace('\u3000\u3000', np.nan)
df = df.drop(0)
df["年"] = [math.floor(i) + 1925 if i > 31 else math.floor(i) + 1988 for i in df["調査項目"]]

plt.plot(df["年"], df["電子レンジ"], marker="o", label="電子レンジ")
plt.ylim(0, 100)
plt.xlabel("年")
plt.ylabel("電子レンジの普及率（%）")
plt.savefig("microwave.pdf", format="pdf", dpi=300)

plt.plot(df["年"], df["電気冷蔵庫"], marker="o", label="電気冷蔵庫")
plt.ylim(0, 100)
plt.xlabel("年")
plt.ylabel("電子レンジと電気冷蔵庫の普及率（%）")
plt.legend(reverse=True, loc='upper left')
plt.savefig("microwave+refrigerator.pdf", format="pdf", dpi=300)

plt.plot(df["年"], df["乗用車"], marker="o", label="乗用車")
plt.ylim(0, 100)
plt.xlabel("年")
plt.ylabel("電子レンジと電気冷蔵庫と乗用車の普及率（%）")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().get_legend().remove()
matplotx.line_labels()
plt.savefig("microwave+refrigerator+car.pdf", format="pdf", dpi=300, bbox_inches='tight')

