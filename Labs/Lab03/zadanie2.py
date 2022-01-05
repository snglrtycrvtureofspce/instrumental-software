from math import*

a = 20.3

x = int(input("Введите x: "))

if x > 1:
  f = log(x + 1)
  print("Ответ идёт по первой ветви")
elif x <= 1:
  f = pow(sin(sqrt(a * x)), 2)
  print("Ответ идёт по второй ветви")


print(f)

# -