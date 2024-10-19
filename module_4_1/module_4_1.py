from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3) # 23.0
result2 = fake_divide(3, 0) # Ошибка, операция невозможна
result3 = true_divide(49, 7) # 7.0
result4 = true_divide(15, 0) # inf
print(result1)
print(result2)
print(result3)
print(result4)