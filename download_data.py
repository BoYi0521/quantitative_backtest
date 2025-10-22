"""
数据下载模块
功能: 从yfinance下载股票历史数据并保存到CSV
作者: [BOYI XIA]
日期: 2025-10-20
"""
import yfinance as yf
import pandas as pd
import os
import datetime

def download_stock_data(ticker, start_date, end_date, save_path):
    """
    下载股票数据

    参数:
        ticker: 股票代码(如 '600519.SS')
        start_date: 开始日期 'YYYY-MM-DD'
        end_date: 结束日期
        save_path: 保存路径

    返回:
        DataFrame: 股票数据
    """

    # 数据的下载
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # 检查数据
    print(f"数据形状: {stock_data.shape}")
    print(f"日期范围: {stock_data.index[0]} 到 {stock_data.index[-1]}")
    print("数据概况")
    print(stock_data.head())

    # 数据保存
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    filename = f"{save_path}/{ticker}.csv"
    stock_data.to_csv(filename) # 将行索引省去
    print(f"\n数据成功保存到: {filename}")

    return stock_data

if __name__ == "__main__":
    TICKER = "002664.sz"
    START_DATE = "2025-01-01"
    END_DATE = "2050-12-31"

    data = download_stock_data(ticker=TICKER, start_date=START_DATE, end_date=END_DATE, save_path="data")

    print("\n数据统计:")
    print(data.describe())



