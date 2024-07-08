from pathlib import Path

import numpy as np
import pandas as pd

# import polars as pl

# 完整版行情结构体
CThostFtdcDepthMarketDataField = np.dtype([
    ('TradingDay', 'S9'),
    ('reserve1', 'S31'),
    ('ExchangeID', 'S9'),
    ('reserve2', 'S31'),
    ('LastPrice', '<f8'),
    ('PreSettlementPrice', '<f8'),
    ('PreClosePrice', '<f8'),
    ('PreOpenInterest', '<f8'),
    ('OpenPrice', '<f8'),
    ('HighestPrice', '<f8'),
    ('LowestPrice', '<f8'),
    ('Volume', '<i4'),
    ('Turnover', '<f8'),
    ('OpenInterest', '<f8'),
    ('ClosePrice', '<f8'),
    ('SettlementPrice', '<f8'),
    ('UpperLimitPrice', '<f8'),
    ('LowerLimitPrice', '<f8'),
    ('PreDelta', '<f8'),
    ('CurrDelta', '<f8'),
    ('UpdateTime', 'S9'),
    ('UpdateMillisec', '<i4'),
    ('BidPrice1', '<f8'),
    ('BidVolume1', '<i4'),
    ('AskPrice1', '<f8'),
    ('AskVolume1', '<i4'),
    ('BidPrice2', '<f8'),
    ('BidVolume2', '<i4'),
    ('AskPrice2', '<f8'),
    ('AskVolume2', '<i4'),
    ('BidPrice3', '<f8'),
    ('BidVolume3', '<i4'),
    ('AskPrice3', '<f8'),
    ('AskVolume3', '<i4'),
    ('BidPrice4', '<f8'),
    ('BidVolume4', '<i4'),
    ('AskPrice4', '<f8'),
    ('AskVolume4', '<i4'),
    ('BidPrice5', '<f8'),
    ('BidVolume5', '<i4'),
    ('AskPrice5', '<f8'),
    ('AskVolume5', '<i4'),
    ('AveragePrice', '<f8'),
    ('ActionDay', 'S9'),
    ('InstrumentID', 'S81'),
    ('ExchangeInstID', 'S81'),
    ('BandingUpperPrice', '<f8'),
    ('BandingLowerPrice', '<f8'),
], align=True)

# TODO：行数，请在每天接收最大数据量上再扩充一些，防止溢出
ROW_COUNT = 8 * 3600 * 2 * 4

filename = r'demo/ctp.bin'
if Path(filename).exists():
    # 以读模式打开，不占用文件
    arr = np.memmap(filename, dtype=CThostFtdcDepthMarketDataField, shape=(ROW_COUNT,), mode='r')
else:
    # 清空并占用了文件，创建后需要立即释放
    arr = np.memmap(filename, dtype=CThostFtdcDepthMarketDataField, shape=(ROW_COUNT,), mode='w+')
    arr = np.memmap(filename, dtype=CThostFtdcDepthMarketDataField, shape=(ROW_COUNT,), mode='r')

# 打印转DataFrame格式
print(pd.DataFrame(arr))
# print(pl.from_numpy(arr))


while True:
    x = input('输入`q`退出；输入其它键打印最新数据')
    if x == 'q':
        break
    # 打印最新的5条
    m = (arr['ClosePrice'] == 0).argmax()
    a = arr[:m]
    print(m, a[-5:], sep='\n')
