a = float(input("Введите 1-ый катет: "))
b = float(input("Введите 2-ой катет: "))
s = a*b/2
from math import sqrt          
c = float(sqrt(a**2 + b**2))
p = a + b + c          

print("Площадь:", s, "периметр:", p)         
