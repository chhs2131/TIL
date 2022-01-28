if __name__ == "__main__":
    # 입력
    n = int(input())
    word = []
    for i in range(0, n):
        word.append(list(input()))

    # 연산
    good_word = 0
    for w in word:
        focus = ""
        flag = False
        left = 0
        right = 0
        for i in range(0, len(w)):
            before = focus
            focus = w.pop()
            if focus == before:  # 이전 알파벳과 같은 글자라면
                left = left - 1
                right = right - 1
                if flag:
                    flag = False
                    left = left + 1
                else:
                    flag = True
                    right = right + 1
            else:
                if flag:
                    right = right + 1
                else:
                    left = left + 1

        if left - right == 0:
            good_word = good_word + 1

    # 출력
    print(good_word)
