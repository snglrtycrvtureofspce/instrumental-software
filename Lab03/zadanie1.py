from math import*
n = int(input("Введите n:"))
sum = 0
x = 0
for i in range(n):
	x = int(input())
	if x % 5 == 0:
		sum = x
print("Сумма:", sum)

# +