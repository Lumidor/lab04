errors = 0
num = 0
while num <= 0:
    num = int(input('Введите целое число: '))
    if num <= 0:
        errors += 1
print(f'Квадрат: {num ** 2}')
print(f'Ошибок: {errors}')
