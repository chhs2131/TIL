import lib.csv_file_reader as csv_file_reader
import lib.heatmap as heatmap
import lib.linear as linear

CSV_FILE_PATH = './lib/test.csv'

# CSV 파일 불러오기
csv_file = csv_file_reader.CsvFile()
csv_file.read(CSV_FILE_PATH)
csv_file.dropna()
csv_file.describe()
csv_data = csv_file.get_csv_file()

# 데이터 상관관계 확인
heatmap.Heatmap(csv_data).show()

# 사용할 컬럼 선정
x = csv_data[['Alcohol', 'percentage expenditure', 'Polio', ' BMI ', 'GDP', ' thinness  1-19 years']]
y = csv_data['Life expectancy ']

# 학습 진행
model = linear.Linear(x, y)
model.fit()
