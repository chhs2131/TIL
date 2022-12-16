import lib.csv_file_reader as csv_file_reader
import lib.heatmap as heatmap
import lib.linear as linear

DATA_PATH = 'data/data.csv'
DATA_WITHOUT_COVID_PATH = 'data/data_without_covid.csv'


def corr_check(CSV_FILE_PATH, repeat_n):
    # CSV 파일 불러오기ㅏ
    csv_file = csv_file_reader.CsvFile()
    csv_file.read(CSV_FILE_PATH)
    csv_file.dropna()
    csv_file.describe()
    csv_data = csv_file.get_csv_file()

    # 데이터 상관관계 확인
    heatmap.Heatmap(csv_data).show()

    # 사용할 컬럼 선정
    # x = csv_data[['premium', 'gasoline', 'light']]
    x = csv_data[['gasoline']]
    y = csv_data['total']

    # 학습 진행 및 결과 확인
    model = linear.Linear(x, y)
    model.fit(repeat_n)


#print("\n===============[코로나포함]=================")
#corr_check(DATA_PATH, 10)
print("\n===============[코로나제외]=================")
corr_check(DATA_WITHOUT_COVID_PATH, 10)
