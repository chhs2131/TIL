def solution(numbers, target):
    # 탐색
    result = [0]
    for n in numbers:
        new_result = []
        for i in range(len(result)):
            new_result.append(result[i] + n)
            new_result.append(result[i] - n)
        result = new_result

    # 갯수 확인
    answer = 0
    for r in result:
        if r == target:
            answer += 1

    return answer
