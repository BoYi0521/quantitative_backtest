"""
库函数import检查模块
功能: 检查所有lib是否可以正常import
作者: [BOYI XIA]
日期: 2025-10-20
"""
import sys

import numpy

print("python version:", sys.version)

try:
    import pandas as pd
    import numpy as np
    import matplotlib
    import yfinance as yf

    print("pandas version:", pd.__version__)
    print("numpy version:", numpy.__version__)
    print("matplotlib version:", matplotlib.__version__)
    print("yfinance version:", yf.__version__)

    print("All libraries imported")
except ImportError as e:
    print("Import failed:", e)