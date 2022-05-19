from collections import defaultdict

a = input()  # 입력은 2000개보다 작음.
n = list(map(int, input().split()))
n.sort()

int_dict = defaultdict(int)
for number in n:
    int_dict[number] += 1

good = 0
len_n = len(n)
if len_n >= 3:
    for target in range(0, len_n):  # 앞에서부터 하나씩 good 인지 탐색\
        # print("#################", n[target])
        for i in range(0, len_n):
            if target == i:  # target과 같은 index를 가르키고 있으면 continue
                continue
            need_number = n[target] - n[i]
            # print("#"+str(i), n[i])
            if int_dict[need_number] != 0:  # 필요숫자가 존재하면서
                if n[i] == need_number == n[target]:  # 필요숫자가 현재 선택된 숫자고, Target 숫자이면 3개 이상 존재해야함.
                    if int_dict[need_number] > 2:
                        # print("  good0", "need(index)", need_number, int_dict[need_number], "now_number", n[i])
                        good += 1
                        break
                elif need_number == n[i] or need_number == n[target]:  # 필요숫자가 현재 선택된 숫자면 해당 숫자가 2개 이상 존재해야함.
                    if int_dict[need_number] > 1:
                        # print("  good1", "need(index)", need_number, int_dict[need_number], "now_number", n[i])
                        good += 1
                        break
                else:
                    # print("  good2", "need(index)", need_number, int_dict[need_number], "now_number", n[i])
                    good += 1
                    break

print(good)
