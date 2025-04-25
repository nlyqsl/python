# import akshare as ak
# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
# pd.set_option('display.max_columns', None)

# #%%
# df = ak.fund_fh_rank_em()
# print(df.head())
# df = df[df['基金简称'].str.contains('REIT')]
# print(df.head())
# #%%
# df2 = df.reset_index(drop=True)
# df2.drop("序号", axis=1, inplace=True)
# print(len(df2))
# print(df2)

# #%%
# df3 = ak.fund_name_em()
# df3 = df3[df3['基金类型'] == 'Reits'].drop(['拼音缩写','拼音全称'],axis=1)
# print(df3)

url = 'https://fundf10.eastmoney.com/fhsp_180101.html'
resp = pd.read_html(url)
print(resp[1])



