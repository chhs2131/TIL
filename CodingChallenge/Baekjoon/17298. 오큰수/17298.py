a = input()
n = list(map(int, input().split()))

len_n = len(n)
result = [-1] * len_n
s = []
for i in range(0, len_n):
    while s:
        s_i = s.pop()
        # print(n[s_i], "vs", n[i], n[s_i] < n[i])
        if n[s_i] < n[i]:
            result[s_i] = n[i]
        else:
            s.append(s_i)
            break
    s.append(i)

print(str(result).replace(",", "").replace("[", "").replace("]", ""))
