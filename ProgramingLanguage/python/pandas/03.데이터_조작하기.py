import pandas as pd
df = pd.read_csv('./test.csv', index_col=0)  # index_col => 첫번째 열을 인덱스로 사용하겠다는 뜻

# 그룹화 하기
print("\n===[그룹화하기]===")
df['family'] = df['SibSp'] + df['Parch']  # 부모자식형제자매를 모두 더해서 가족으로 만든다.
means = df.groupby('family').mean()  # 가족단위별 다른 변수의 평균 정보를 구한다.
print(means)

# 필터링
print("\n===[필터링]===")
big_family = df['family'] > 4  # 5인이상 대가구 선정
print(df[big_family])  # 가족이 많은사람만 출력되게된다.

# 결측치(null, nan, ... ) 찾기
print("\n===[결측치 찾기]===")
no_age = df['Age'].isna()  # 결측된 곳이 True
print(df[no_age])

# 결측치 제거하기
print("\n===[결측치 제거하기]===")
# axis=0 결측치가 있는 행을 삭제한다. how=any 결측치가 하나라도 있다면 대상, inplace=false 기존 df는 건들이지 않고 새걸 반환한다.
new_df = df.dropna(axis=0, how='any', inplace=False)
print(new_df.count())
print(df.count())

# 결측치 임의값으로 채우기
print("\n===[결측치 임의값으로 채우기]===")
full_df = df.fillna(9999, inplace=False)
print(full_df.count())
print(df.count())
