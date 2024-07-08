# ctp_memmap_demo

使用内存映射文件，`C++`实时录制数据，再通过`numpy`实时读取。

## ctp_mmap.py

演示读取内存映射文件

1. 先配置记录条数，然后运行。会在`demo`目录下创建`ctp.bin`文件
2. 按任意键输出最新5条数据
3. 按`q`退出

## demo

演示写入内存映射文件。此项目在`SFIT`的`demo`上直接扩展而成

1. 直接用`Visual Studio`打开`demo_program.sln`，编译成`testprogram.exe`
2. 运行项目，打开`ctp.bin`文件写入数据。注意：只能打开长度不为0的文件，不能主动创建
3. 观察`ctp_mmap.py`的显示输出

## 核心逻辑
1. `C++`项目使用`memmap.hpp`中封装的结构体，实现读内存映射文件。参考`main.h`中的`CSimpleMdHandler`
2. `Python`使用`numpy.memmap`读内存映射文件

## 改进建议

1. 本项目只是一个简单的演示，没有考虑稳定性
2. 记录条数要预留多些。等收盘后结算价也推送完后，截断再备份
3. 不同交易所的交易日处理方式各有不同，成交金额的算法也不一样，可以考虑不同交易所行情存在不同文件
4. 如果要不同交易所套利，可以为每条记录多加一个本地时间。避免行情中的交易所时间误差大

## 参考

- https://github.com/manuel5975p/memmap
- http://www.sfit.com.cn/5_2_DocumentDown_2_2.htm