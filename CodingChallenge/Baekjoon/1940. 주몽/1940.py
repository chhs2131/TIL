if __name__ == "__main__":
    n = int(input())
    m = int(input())
    u = list(map(int, input().split()))
    u.sort()

    i = 0
    j = n - 1
    num_of_armor = 0
    while i<j:
        usum = u[i] + u[j]
        if usum == m:
            num_of_armor = num_of_armor + 1
            i = i + 1
            j = j - 1
        elif usum > m:
            j = j - 1
        elif usum < m:
            i = i + 1

    print(num_of_armor)
