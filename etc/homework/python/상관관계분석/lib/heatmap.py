import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 시각화를 통해 상관관계 파악 (14.23 p61)
# 영향을 미치지 않는 특징들을 모두 포함하여 학습시키면 학습이 잘 되지 않을 수 있음
class Heatmap:
    __data = None

    def __init__(self, data):
        self.__data = data
        self.__validate_data_is_none()

    def show(self):
        self.__validate_data_is_none()

        sns.set(rc={'figure.figsize': (12, 10)})
        correlation_matrix = self.__data.corr().round(2)  # 상관관계를 구한다.
        sns.heatmap(data=correlation_matrix, annot=True)
        plt.show()

    def __validate_data_is_none(self):
        if self.__data is None:
            raise ValueError("data에 값이 없습니다. path에 파일이 있는지 확인해주세요.")


if __name__ == '__main__':
    data = pd.read_csv('./test.csv')
    data.dropna(inplace=True)
    heatmap = Heatmap(data)
    heatmap.show()
