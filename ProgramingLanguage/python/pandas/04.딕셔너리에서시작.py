import pandas as pd

dic = {
    'item': ['old_ring', 'old_ring', 'good_ring', 'good_ring'],
    'type': ['silver', 'gold', 'diamond', 'bronze'],
    'price': ['100', '50', '1000', '200']
}

# 딕셔너리로 부터 데이터프레임 생성
print("\n===[딕셔너리에서 생성]===")
df = pd.DataFrame(dic)
print(df)

# 인덱스 항목 새로 지정
print("\n===[인덱스 항목 새로 지정]===")
df2 = df.pivot(index='item', columns='type', values='price')
print(df2)
