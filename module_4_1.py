"""
Домашняя работа по уроку "Модули и пакеты"
"""

from fake_math import divide as divide_fake_math
from true_math import divide as divide_true_math

result1 = divide_fake_math(69, 3)
result2 = divide_fake_math(3, 0)
result3 = divide_true_math(49, 7)
result4 = divide_true_math(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
