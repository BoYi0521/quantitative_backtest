- 在stock_data.to_csv(filename, index=False)中index=False会将每一行的索引去除,
但是在我们这个任务中第0列是时间,最好不要删去
- 在data = pd.read_csv(file_path, index_col=0, parse_dates=[0])读取数据的时候,
index_col将时间设置为索引, parse_dates=[0]则将可能是时间的内容转为Timestamp
- close_price.pct_change()可以计算出数据每天的涨跌幅
- daily_return = close_price.pct_change(): 计算每天的涨跌幅
  volatility = daily_return.std() * np.sqrt(len(data)) * 100: 每日收益的"标准差"*交易日天数 = 年标准差,
  也就是年标准差(年化波动率)
- rolling()是滚动计算函数,比如data['Close'].rolling(window=short_window).mean()就是滚动计算MA
且会将前window-1的天数自动设置为nan
- diff()则是一阶滚动差分
- 