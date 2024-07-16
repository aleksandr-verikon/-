# 3rd program
num1 = 1234
num2 = 5678
# вычисляем серединные числа
middle1 = ((num1 % 1000) // 10)
middle2 = ((num2 // 10) % 100)
# вычисляем сумму серединных чисел
result = middle1 + middle2
print(result)