from math import*
x = int(input("Введите число a:"))
pi = 3.14
if x == -1:
	print("Значение -1 не обрабатывается")	
elif x == 0:	
	print("Значение 0 не обрабатывается")
else:
	y = pow(cos(exp(x)) + log(1 + x) + sqrt(pow(exp(x), cos(x)) + pow(sin(x), 2) * pi * x) + sqrt(1/x) + pow(cos(x),2),2)
	print("Ответ:", y)
