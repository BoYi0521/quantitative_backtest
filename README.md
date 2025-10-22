# 双均线交易策略回测系统

## 项目简介
这是一个简单的量化交易回测系统,用于测试双均线策略在A股市场的表现。

**核心功能:**
- 下载股票历史数据
- 计算双均线(MA5, MA20)
- 生成买卖信号
- 计算策略收益并可视化

## 技术栈
- Python 3.12
- pandas 2.3.3: 数据处理
- numpy 2.3.4: 数值计算
- matplotlib 3.10.7: 数据可视化
- yfinance 0.2.66: 获取股票数据

## 快速开始

### 安装依赖
```bash
pip install pandas numpy matplotlib yfinance --break-system-packages
```

### 运行
```bash
python backtest.py
```

## 项目结构
```
quantitative_backtest/
├── data/
├── results/
├── download_data.py          # 数据下载
├── explore_data              # 检查数据
├── calculate_indicators.py   # 计算指标(均线)
├── generate_signals.py       # 生成信号
├── calculate_returns.py      # 计算收益
├── visualize_results.py      # 可视化
├── performance_metrics.py    # 性能评估
├── README.md
└── PROJECT_ROADMAP.md
```

## 策略说明

**双均线策略逻辑:**
1. 计算5日均线(MA5)和20日均线(MA20)
2. 当MA5上穿MA20时,产生买入信号
3. 当MA5下穿MA20时,产生卖出信号
4. 简化假设:全仓交易,不考虑手续费(v1版本)

## 回测结果

**测试标的**: 
**测试区间**: 

| 指标 | 买入持有 | 双均线策略 |
|------|----------|-----------|
| 累计收益 | TBD | TBD |
| 最大回撤 | TBD | TBD |
| 夏普比率 | TBD | TBD |

(做完后填入真实数据)

## 后续优化方向
- [ ] 加入交易成本
- [ ] 测试不同均线参数组合
- [ ] 增加止损止盈逻辑
- [ ] 支持批量回测多只股票
- [ ] 加入更多技术指标(MACD, RSI等)


## 参考资料
- [yfinance文档](https://pypi.org/project/yfinance/)
- [pandas时间序列处理](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- 《Python量化交易编程》相关章节

## 作者
[BOYI XIA] - Yale CS  
如有问题欢迎交流: [boyi.xia@yale.edu]

## License
MIT