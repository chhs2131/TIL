from sklearn import linear_model
from sklearn import datasets
import matplotlib.pyplot as plt

diabets = datasets.load_diabetes()
regr = linear_model.LinearRegression()

# 학습용 검증용 데이터로 나누기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    diabets.data,
    diabets.target,
    test_size=0.2  # 20%
)

# 학습진행
regr.fit(x_train, y_train)
print(regr.coef_, regr.intercept_)

y_pred = regr.predict(x_test)
plt.scatter(y_pred, y_test)
plt.show()
