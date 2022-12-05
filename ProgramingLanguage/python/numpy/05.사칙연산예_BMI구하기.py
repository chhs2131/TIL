import numpy as np

BMI_LAMBDA = (lambda h, w: w / (h ** 2))

height = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weight = np.array([86, 74, 59, 95, 80, 68])

print("BMI 결과")
print(BMI_LAMBDA(height, weight))  # [25.68007405 23.88946281 20.65754    27.45982194 25.53544639 22.72043837]
