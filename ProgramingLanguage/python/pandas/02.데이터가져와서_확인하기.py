import pandas as pd

# csv 파일 불러오기
print("\n===[CSV 파일 불러오기]===")
df = pd.read_csv('./test.csv', index_col=0)  # index_col => 첫번째 열을 인덱스로 사용하겠다는 뜻
print(df)

# 특정 열만 불러오기
print("\n===[특정 열만 선택하기]===")
print(df[['Age', 'Pclass']])

# 상위 5개 행만 가져오기 (=df[0:5])
print("\n===[상위 행만 가져오기]===")
print(df.head())
print(df[0:5])

# 데이터프레임 간단하게 분석하기
print("\n===[간단히 분석하기]===")
print('describe', df.describe())
print('count :', df.count())
print('Age mean :', df['Age'].mean())
print('Age std :', df['Age'].std())

# 새로운 열 추가하기
print("\n===[새로운 열 추가하기]===")
df['new_col_price'] = df['Pclass'] * 10
print(df)
