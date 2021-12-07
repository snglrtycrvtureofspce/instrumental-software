from random import randint

def get_multiplier(unit):
    if unit == 2:
        f = "https://pythonru.com/osnovy/cikl-for-in"
    return f
    if unit == 9:
        a = int(input("Введите натуральное число a: "))
        a1 = a / 1000
        print(a1)
        a2 = (a % 1000) / 100
        print(a2)
        a3 = (a % 100) / 10
        print(a3)
        a4 = a % 10
        print(a4)
        if (a1 + a2 == a3 + a4):
            f = "True"
        else:
            f = "False"
        return f
    if unit == 10:
        n = int(input('Введите число n: '))
        count = 0
        for i in range(100, 1000):
            summ = 0
            for j in str(i):
                summ += int(j)
            if summ == n:
                count += 1
        return count
    if unit == 14:
        a = float(input())
        a = a - int(a)
        for i in range(5):
            if int(a) == 7:
                print('Есть')
                break
            a = a * 10 
        else:
            print('Нету')
        return 'конец'
    if unit == 21:
        n = int(input("Введите размер одномерного массива: "))
        arr = [0] * n
        for i in range(n):
            arr[i] = randint(10,20)
        for i in range(n):
            if (arr[i] % 2 == 0 and i % 3 == 0):
                print(arr[i])
        return "конец"
    if unit == 22:
        rows = int(input("Введите размер строк в двумерном массиве: "))
        cols = int(input("Введите размер столбцов в двумерном массиве: "))
        m=[[randint(-30,30) for i in range(cols)] for j in range(rows)]
        for i in m:
            print(*i,sep='\t')
        print("___________________________________________")

        for i in range(len(m)):
            for j in range(i):
                if (i < j):
                    print(*i, sep = '\t')


        mx=-11
        for i in range(len(m)):
            for j in range(i):
                mx=m[i][j] if mx<m[i][j] else mx

        summ=0
        for i in range(1,len(m)+1):
            for j in range(1,i+1):
                summ+=m[-i][-j] if mx<m[-i][-j] else 0
        return 4
    if unit == 24:
        n = int(input("Введите размер одномерного массива: "))
        arr = [0] * n
        for i in range(n):
            arr[i] = randint(10,200)
        for i in range(n):
            if (arr[i] % 2 == 0):
                print(i)
        return "конец"
    raise ValueError('Undefined unit: {}'.format(unit))

unit = int(input("Введите номер задания: "))
print(get_multiplier(unit))
