# 4th program
num1 = 13.42
num2 = 42.13
# Извлекаем целую и дробную части
int_part1 = int(num1)
frac_part1 = int((num1 * 100) % 100)
int_part2 = int(num2)
frac_part2 = int((num2 * 100) % 100)
# Проверяем условия
if int_part1 == frac_part2 or int_part2 == frac_part1:
    print("True")
else:
    print("False")