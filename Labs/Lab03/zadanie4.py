i = 1

n = int(input("Введите число N: "))
for i in range(n):
    if i < n:
        ++i
        a = i
        b = i
        if (i % 10 == 0):
            continue
        while (b != 0):
            if (b % 10 == 0):
                continue
            if (a % (b % 10) == 0):
                b = b / 10
            else:
                break
        if (b == 0):
            print(a)
# -