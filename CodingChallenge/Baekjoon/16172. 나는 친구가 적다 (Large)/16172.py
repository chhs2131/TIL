import re

sentence = input()
key = input()

sentence = re.sub("\d", "", sentence)  # 숫자 제거
if re.search(key, sentence) is None:  # 단어 찾기
    print(0)
else:
    print(1)
