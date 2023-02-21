n, new_record, limit = map(int, input().split())

rank = -1
if n == 0:
    rank = 1
else:
    record = list(map(int, input().split()))

    now_score = -1
    for i in range(n):
        score = record[i]
        print(new_record, score)
        if score < new_record:
            print("great")
            if now_score == -1:
                rank = i + 1
            break
        elif score == new_record and i != limit - 1 and now_score != score:
            print("same")
            now_score = score
            rank = i + 1

        if i >= limit - 1:
            print("?")
            print("now", now_score, new_record)
            if now_score == new_record:
                print("?!")
                rank = -1
            break

print(rank)
