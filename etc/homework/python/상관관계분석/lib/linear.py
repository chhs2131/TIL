import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


class Linear:
    __x = None
    __y = None

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__validate_data_is_none()

    def __validate_data_is_none(self):
        if self.__x is None or self.__y is None:
            raise ValueError("Data is None")

    def __split_data(self, test_size):
        # 데이터 나누기
        x_train, x_test, y_train, y_test = train_test_split(self.__x, self.__y, test_size=test_size)
        return x_train, x_test, y_train, y_test

    def fit(self, repeat_n=1):
        for i in range(repeat_n):
            # 데이터를 학습용/검증용으로 나눔
            x_train, x_test, y_train, y_test = self.__split_data(test_size=0.2)
            print("\n===[ 학습 개요 ]===")
            print("테스트(train) 데이터 갯수: ", len(y_train))
            print("검증(test) 데이터 갯수: ", len(y_test))

            # 학습 진행
            lin_model = LinearRegression()
            lin_model.fit(x_train, y_train)
            y_test_predict = lin_model.predict(x_test)

            # 모델 오차 확인
            rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))
            print("rmse(평균제곱근오차) #" + str(i), rmse)

            # 시각화
            graph_title = 'graph #' + str(i)
            plt.title(graph_title)
            # plt.scatter(y_test, y_test_predict)  # 실제 결과와 예측값 관의 관계
            plt.scatter(np.array(x_test), np.array(y_test))  # 실제 결과와 예측값 관의 관계
            # plt.plot(y_test, y_test, color="red")
            plt.plot(x_test, lin_model.predict(x_test), color='green')
            plt.savefig(graph_title + '.png',
                        facecolor='#eeeeee',
                        edgecolor='black',
                        format='png', dpi=100,
                        bbox_inches='tight')
            plt.show()
            plt.close()


if __name__ == '__main__':
    # 데이터를 불러오고 결측치를 제거
    life = pd.read_csv('./test.csv')
    print(life.count())
    print(life.shape)
    print(life.isnull().sum())
    life.dropna(inplace=True)

    # 시각화를 통해 상관관계 파악 (14.23 p61)
    # 영향을 미치지 않는 특징들을 모두 포함하여 학습시키면 학습이 잘 되지 않을 수 있음
    import matplotlib.pyplot as plt

    sns.set(rc={'figure.figsize': (12, 10)})
    correlation_matrix = life.corr().round(2)
    sns.heatmap(data=correlation_matrix, annot=True)
    plt.show()

    # 사용할 컬럼 선정
    x = life[['Alcohol', 'percentage expenditure', 'Polio', ' BMI ', 'GDP', ' thinness  1-19 years']]
    y = life['Life expectancy ']

    # 학습하여 결과 확인
    linear = Linear(x, y)
    linear.fit()
