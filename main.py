import math 
x = float(input("Введите значение x: ")) 
y = float(input("Введите значение y: ")) 
num1_chisl = (8 + abs(x - y) **  2) ** (1/3) + 1 
num1_znam = x ** 2 + y ** 2 + 2 
num2 = math.exp(x - y) 
u = num1_chisl / num1_znam - num2 
print("Значение функции u:", u)