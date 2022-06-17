'''
Вариант 11
1) Так выглядит функция-декоратор. 
Принимает в качестве аргумента другую функцию. 
Затем с этой функцией что-то делают внутри вложенной функции-обёртки и возвращают из декоратора уже обёртку вместо исходной функции.
Пример:
@decorator_function
def privet():
	print("privet!")
privet()
2) Requests позволяет легко и с минимальным количеством кода взаимодействовать с веб-приложениями. 
Это необходимо для решения любых задач, связанных с передачей информации от пользоватепя к серверу и обратно.
Пример:
import requests
url = "https://google.com"
image = requests.get(url)
'''
import math
class circle:
	# Инициализация
	def __init__(self):
		pass
	# Деструктор
	def __del__(self):
		pass
	# Первый сеттер
	def set_first_r(self, r1):
		self.r1 = r1
	# Второй сеттер
	def set_second_r(self, r2):
		self.r2 = r2
	# Первый геттер
	def get_first_r(self):
		return self.r1
	def get_second_r(self):
	# Второй геттер
		return self.r2
	# Выводит информацию о двух радиусах окружностей на экран
	def display_info(self):
		print(f'r1: {self.r1}')
		print(f'r2: {self.r2}')
	#  Считает и выводит площадь двух окружностей
	def display_area(self):
		s = math.pi * math.pow(self.r1, 2)
		s2 = math.pi * math.pow(self.r2, 2)
		print(f'First area: {s}')
		print(f'Second area: {s2}')
	# Количество процентов, которое занимает один круг от другого
	def procent(self):
		p = ((self.r1 / self.r2) * 0.1)
		print(f'Procent: {p}')

First_circle = circle()
First_circle.set_first_r(2)
First_circle.set_second_r(4)
First_circle.display_info()
del First_circle

print("_________________________________________________________\n")

Second_circle = circle()
Second_circle.set_first_r(10)
Second_circle.set_second_r(20)
print(Second_circle.get_first_r())
print(Second_circle.get_second_r())
Second_circle.display_area()
Second_circle.procent()
del Second_circle