# 每日工作日志

## 使用说明
1.记录当天遇到的问题以及解决方法
**遇到的问题:**
...
**解决方案:**
...

2.记录下一次需要完成的工作任务
**一个工作日的任务**
- ...
- ...
- 
3.对当天工作的总结
**学习到的知识:**
- ...
- ...

## 2025/10/20

## 2025/10/21

**遇到的问题:**
在我们探索数据close_price的类型是object而非float(),不能直接使用max()比较这导致了报错
**解决方案:**
编写一个数据清洗function将所有的object数据用pd.to_numeric()转换类型转为float()类型

**遇到的问题:**
Date作为行索引的表头在date这一行本身就没有任何的数据,全为null,这会影响到数据中缺省值的检测
**解决方案:**
在观察缺省值的时候零时忽略:data_no_index_na = data.dropna(how='all')  # 去掉整行都是 NaN 的
或者: missing_rows = data[data.isna().any(axis=1)]只检查数据列不讲index当成一列

**下一个工作日的任务**
- 完成数据清洗function: def clean_data(data):
  - 实现数据类型的转换
  - 如果存在缺失值将该行数据作废
- 检查数据完整性的function完善,解决行索引也被纳入缺失值检查的问题def check_data_quality(data):
- 价格走势图的绘制(k线图)
- 详细价格图的绘制

**今天学习到的新知识**
- 波动性的概念以及计算方式
- 在处理数据之前,查看数据的数据结构是很重要的

## 2025/10/22

**遇到的问题:**
在数据类型转换和统计缺省值的时候总会将第一行的股票代码和第二行的date行纳入,但是我们不需要这个
**解决方案:**
直接在读取的时候skip这两行

**遇到的问题:**
直接使用data = pd.read_csv(file_path, skiprows=[0,1], index_col=0, parse_dates=True)
会导致列名消失:['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']
而在使用dropna('Close')的时候就会产生错误
**解决方案:**
直接重新赋名,安排index:
data = pd.read_csv(
        file_path,
        skiprows=[0,1],
        names=['Date', 'Close', 'High', 'Low', 'Open', 'Volume'],
        parse_dates=['Date'],
        index_col='Date'
    )

**遇到的问题:**
在plot图标的时候需要ticker作为label但是我们在load_data的时候直接跳过了一二行导致无法提取到
**解决方案:**
可以直接从文件名中提取到ticker

**下一个工作日的任务**
- 

**今天学习到的新知识**
- 我们昨天在考虑的问题2,其实这个行索引的表头date不是数据本身,而是多重索引中的结构,
所以data.dropna(how='all')不会删去改行
并且missing = data.isnull().sum()统计缺失值也不会计入这一行