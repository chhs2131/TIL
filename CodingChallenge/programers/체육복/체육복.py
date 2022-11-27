def solution(n, lost, reserve):
    # 여분 있는 사람이 잃어버렸는지 확인
    new_lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)

    # 잃어버린 사람에 앞 뒷 사람에게 여벌이 있는지 확인한다.
    for l in new_lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer += 1
    return answer
