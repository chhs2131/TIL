import pandas as pd
import seaborn as sns

# 데이터를 불러오고 결측치를 제거
life = pd.read_csv('./who_life.csv')
print(life.count())
print(life.shape)
print(life.isnull().sum())
life.dropna(inplace=True)

# 시각화를 통해 상관관계 파악 (14.23 p61)
# 영향을 미치지 않는 특징들을 모두 포함하여 학습시키면 학습이 잘 되지 않을 수 있음
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(12,10)})
correlation_matrix = life.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()

# 사용할 컬럼 선정
x = life[['Alcohol', 'percentage expenditure', 'Polio', ' BMI ', 'GDP', ' thinness  1-19 years']]
y = life['Life expectancy ']

# 데이터 나누기
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# 학습 진행
from sklearn.linear_model import LinearRegression
lin_model = LinearRegression()
lin_model.fit(x_train, y_train)
y_test_predict = lin_model.predict(x_test)

# 모델 오차 확인
import numpy as np
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))
print("rmse(평균제곱근오차)", rmse)

# 시각화
plt.scatter(y_test, y_test_predict)
plt.show()
