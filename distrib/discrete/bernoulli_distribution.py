#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/10/9 14:53
# @Author : qizheng
# @File : bernoulli_distribution.py
# @Proj : ProbabilityDistribution
# @Software: PyCharm
import scipy
import numpy as np
import pandas as pd
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
p = 0.3
mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
x = np.arange(bernoulli.ppf(0.01, p), bernoulli.ppf(0.99, p))
ax.plot(x, bernoulli.pmf(x, p), 'bo', ms=8, label='bernoulli pmf')
ax.vlines(x, 0, bernoulli.pmf(x, p), colors='b', lw=5, alpha=0.5)
rv = bernoulli(p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()
