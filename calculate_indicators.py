"""
以短期,长期均价为技术指标的计算模块
功能: 计算移动平均线等技术指标
日期: 2025/10/25
"""

import pandas as pd
import numpy as np

def calculate_moving_averages(data, short_window=5, long_window=10):
    """
    计算移动平均线

    参数:
        data: DataFrame,必须包含'Close'列
        short_window: 短期窗口(默认5日)
        long_window: 长期窗口(默认20日)

    返回:
        DataFrame: 添加了MA列的数据

    原理:
        MA5 = 最近5天收盘价的平均值
        使用pandas的rolling()函数实现滚动计算
    """

    print("\n" + "=" * 50)
    print("计算移动平均线")
    print("=" * 50)

    if 'Close' not in data.columns:
        raise ValueError("data中缺失'Close'列")

    print(f"\n计算 {short_window}日均线 和 {long_window}日均线...")

    # 计算短期均线(MA5),存储在'MA_short'与'MA_long'column中
    # 不过将窗口大小保存到列名更佳
    data[f"MA{short_window}"] = data['Close'].rolling(short_window).mean()
    data[f"MA{long_window}"] = data['Close'].rolling(long_window).mean()

    # 统计有效数据
    valid_short = data[f"MA{short_window}"].notna().sum()
    valid_long = data[f"MA{long_window}"].notna().sum()
    print(f"\nMA{short_window} 有效数据: {valid_short} 天")
    print(f"MA{long_window} 有效数据: {valid_long} 天")

    return data

def analyze_ma_crossover(data):
    """
    分析均线交叉情况

    找出金叉(MA5上穿MA20)和死叉(MA5下穿MA20)
    """

    data['MA5_above_MA20'] = data['MA5'] > data['MA20']

    data['Crossover'] = data['MA5_above_MA20'].astype(int).diff()

    golden_cross = data[data['Crossover'] == 1]
    death_cross = data[data['Crossover'] == -1]

    print(f"\n金叉次数: {len(golden_cross)}")
    print(f"死叉次数: {len(death_cross)}")

    if len(golden_cross) > 0:
        print(f"\n最近一次金叉: {golden_cross.index[-1]}")
        print(golden_cross[['Close', 'MA5', 'MA20']].tail(1))

    if len(death_cross) > 0:
        print(f"\n最近一次死叉: {death_cross.index[-1]}")
        print(death_cross[['Close', 'MA5', 'MA20']].tail(1))

    return data

if __name__ == "__main__":
    file_path = "data/002664.sz.csv"
    data = pd.read_csv(
        file_path,
        skiprows=[0, 1],
        names=['Date', 'Close', 'High', 'Low', 'Open', 'Volume'],
        parse_dates=['Date'],
        index_col='Date'
    )

    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # 1. 计算均线
    data = calculate_moving_averages(data, short_window=5, long_window=20)

    # 2. 分析交叉
    data = analyze_ma_crossover(data)

    # 3. 查看最新数据
    print("\n" + "=" * 50)
    print("最新10天数据")
    print("=" * 50)
    print(data[['Close', 'MA5', 'MA20']].tail(10))

    print("\n 均线计算模块测试完成!")