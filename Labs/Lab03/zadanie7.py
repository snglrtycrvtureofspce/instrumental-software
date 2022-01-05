k = 0
r = 0
i = 3
n = int(input("Введите количество чисел: "))
l = int(input("Введите первое число: "))
x = int(input("Введите следующее число: "))
if x > l:
    k = k + 1
for i in range(n):
    l = x   
    x = r
    r = int(input("Введите следующее число: "))
    if x > l and x > r:
        k = k + 1
            
print("Количество чисел больше своих соседей: ", k)

# -