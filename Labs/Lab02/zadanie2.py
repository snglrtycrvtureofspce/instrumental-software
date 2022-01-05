import math 
x = float(input("Введите число a:"))
y = float(input("Введите число y:"))
if x <= 1 and x >= -1 and y <= 1 and y >= -1:
	print("Точка лежит на плоскости")
else:
	print("Точка не лежит на плоскости")