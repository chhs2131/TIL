from sklearn import linear_model

regr = linear_model.LinearRegression()
x = [[164], [179], [162], [170]]  # x는 다차원 배열이여야 한다.
y = [53, 63, 55, 59]
regr.fit(x, y)  # 학습

# 실제 모델 사용해보기
input_data = [[180], [160]]
result = regr.predict(input_data)
print(result)


# 예측 결과를 그래프로 확인해보기
import matplotlib.pyplot as plt

plt.scatter(x, y, color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.show()
