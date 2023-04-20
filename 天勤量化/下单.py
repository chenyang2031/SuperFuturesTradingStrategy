# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:06:06 2023

@author: lenovo
"""
from tqsdk import TqApi, TqAuth, TqKq, TqAccount
api = TqApi(web_gui=True, auth=TqAuth("16673287082", "13787489651"))
# quote = api.get_quote("SHFE.ni2206")
# api = TqApi(TqAccount("S神华期货", "6110502", ""),web_gui=True, auth=TqAuth("16673287082", "13787489651"))
# quote = api.get_quote("SHFE.ni2206")
# print(quote.last_price, quote.volume)

# 订阅 ni2010 合约的10秒线
klines = api.get_kline_serial("DCE.c2305", 10)

order = api.insert_order(symbol="DCE.m2005", direction="BUY", offset="OPEN", volume=5, limit_price=2900)

while True:
    # 通过wait_update刷新数据
    api.wait_update()









