"""
数据探索模块
功能: 检查csv数据并进行基础分析
作者: [BOYI XIA]
日期: 2025/10/21 & 2025/10/22
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from matplotlib.pyplot import ylabel, xlabel


def load_data(file_path):
    """
    读取CSV数据

    参数:
        filepath: CSV文件路径

    返回:
        DataFrame: 股票数据
    """
    print(f"正在读取: {file_path}")
    data = pd.read_csv(
        file_path,
        skiprows=[0,1],
        names=['Date', 'Close', 'High', 'Low', 'Open', 'Volume'],
        parse_dates=['Date'],
        date_format='%Y-%m-%d',
        index_col='Date'
    )

    print("数据读取成功")
    print(f"数据形状: {data.shape} (行,列)")
    print(f"日期范围: {data.index[2]} 到 {data.index[-1]}")
    print(f"观测的总交易日: {len(data)-1}") # load_data在数据清洗之前,将索引行也纳入统计了

    return data


def clean_data(data):
    """
    清洗数据

    处理:
    1. 删除完全为空的行
    2. 将数值列转换为正确的类型
    3. 处理缺失值
    """
    print("\n" + "=" * 50)
    print("数据清洗")
    print("=" * 50)

    print(f"原始数据形状: {data.shape}")

    # 1. 删除完全为空的行
    data = data.copy()
    data = data.dropna(how='all')  # 不会删除多重索引中的列索引

    # 确保索引仍然是 DatetimeIndex
    if not isinstance(data.index, pd.DatetimeIndex):
        print("⚠️ 索引类型已改变，正在修复...")
        data.index = pd.to_datetime(data.index)

    # 2. 将价格和成交量转换为float类型
    numeric_columns = ['Close','High','Low','Open','Volume']

    print("\n[原始数据类型]")
    print(data.dtypes)

    for column in numeric_columns:
        if column in data.columns: # 判断列明是不是真实存在于DataFrame
            data[column] = data[column].astype(float)

    print("\n[转换后数据类型]")
    print(data.dtypes)

    # 3. 缺失值统计
    print("\n[缺失值统计]")
    missing = data.isnull().sum() # 这个.sum()得到一个series
    if missing.sum() > 0: # 将每个col缺失的数值数量加起来
        print("存在缺失值")
    else:
        print("不存在缺失值")

    # 4. 删除缺少收盘价这一关键值的行
    # 先打印列名
    print(data.columns.tolist())
    before_drop = len(data)
    data = data.dropna(subset=['Close'])
    after_drop = len(data)

    if before_drop > after_drop:
        print(f"删除了 {before_drop - after_drop} 行数据(收盘价缺失)")

    print(f"\n清洗后数据形状: {data.shape}")
    print(f"日期范围: {data.index[0]} 到 {data.index[-1]}")

    return data



def check_data_quality(data):
    """
    检查数据质量

    检查项:
    1. 缺失值
    2. 数据类型
    3. 基本统计
    """

    print("\n" + "="*50)
    print("数据质量检测")
    print("="*50)

    # 1. 查看数据结构
    # 这部分的实现转移到了数据清洗function中
    """print("\n[数据列信息]")
    print(data.columns.tolist())"""

    # 2. 检查缺失值
    # 这部分的实现转移到了数据清洗function中
    """missing = data.isnull().sum()
    if missing.sum() == 0:
        print("不存在缺失值")
    else:
        print(f"存在缺失值")"""


    # 3. 查看数据类型
    print("\n[数据类型]")
    print(data.dtypes)

    # 4. 基本数据统计
    print("\n[基本数据]")
    print(data.describe())

    return data


def analyze_data(data):
    """
        分析价格数据
        """
    print("\n" + "=" * 50)
    print("价格分析")
    print("=" * 50)

    close_price = data['Close']

    # 基本统计
    print(f"\n收盘价统计:")
    print(f"  最高收盘价: ¥{close_price.max():.2f}")
    print(f"  最低收盘价: ¥{close_price.min():.2f}")
    print(f"  平均收盘价: ¥{close_price.mean():.2f}")
    print(f"  最近收盘价: ¥{close_price.iloc[-1]:.2f}")

    # 计算涨跌幅
    total_return = (close_price.iloc[-1] / close_price.iloc[0] - 1) * 100
    print(f"\n从{data.index[2]} 到 {data.index[-1]}期间涨跌幅为: {total_return:+.2f}%")

    # 波动性
    daily_return = close_price.pct_change()
    volatility = daily_return.std() * np.sqrt(len(data)) * 100
    print(f"2025/1/1截止目前共: {len(data)} 天交易日的波动率为: {volatility:.2f}%")

    return data


def plot_price(data, ticker):
    fig, ax = plt.subplots()
    ax.plot(data['Close'], label='close price', color='blue', linewidth=1)
    ax.set_title(f'{ticker} price trend', fontsize=16, fontweight='bold')
    ax.set_xlabel('date', fontsize=12)
    ax.set_ylabel('price', fontsize=12)
    ax.grid(True,alpha=0.3)
    ax.legend(loc='best')
    plt.tight_layout()

    output_path = 'results/price_trend.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print("price trend saved successfully")
    plt.show()

    return fig


def plot_ohlc(data, ticker):
    mc = mpf.make_marketcolors(up='red', down='green', edge='inherit', wick='inherit')
    s = mpf.make_mpf_style(marketcolors=mc)

    save_path = 'results/ohlc.png'

    mpf.plot(
        data,
        type='candle',
        volume=True,
        title=f"{ticker} ohlc",
        ylabel="price",
        xlabel="volume",
        savefig=save_path
    )

    print("ohlc saved successfully")

    return save_path



if __name__ == "__main__":
    file_path = "data/002664.sz.csv"
    data = load_data(file_path)
    ticker = file_path.replace('data/','').split('.')[0]
    data = clean_data(data)
    data = check_data_quality(data)
    data = analyze_data(data)
    plot_price(data, ticker)
    plot_ohlc(data, ticker)

    print("探索完毕")
