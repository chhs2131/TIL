import numpy as np
import pandas as pd

# 시리즈
print("=====[시리즈]=====")
series = pd.Series([1, 3, 4, np.nan, 6, 8])
print(series)

# 데이터 프레임
print("\n=====[데이터프레임]=====")
series2 = pd.Series([6,5,4,3,2,1])
series3 = pd.Series([1,10,100,1000,10000,100000])

df = pd.DataFrame({'번호': series,
                   '등급': series2,
                   '잔액': series3})
print(df)

