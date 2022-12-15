import pandas as pd


class CsvFile:
    def __init__(self):
        self.__csv_file = None

    def read(self, file_path):
        self.__csv_file = self.__read_csv_file(file_path)

    def __read_csv_file(self, file_path):
        return pd.read_csv(file_path)

    def describe(self):
        print("\n===[항목별 개수 출력]===")
        print(self.__csv_file.count())
        print("\n===[항목 형태 출력]===")
        print(self.__csv_file.shape)
        print("\n===[비어있는칸 개수 출력]===")
        print(self.__csv_file.isnull().sum())

    def dropna(self):
        self.__csv_file.dropna(inplace=True)

    def get_csv_file(self):
        return self.__csv_file


if __name__ == '__main__':
    csv_file = CsvFile()  # 객체 생성
    csv_file.read('test.csv')  # 명시된 경로에 있는 파일을 읽어옴
    csv_file.describe()  # 파일 정보를 출력
