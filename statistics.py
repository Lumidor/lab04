n = int(input('Введите кол-во чисел n (n >= 1): '))
first_num = int(input('Введите 1-е число: '))
total_sum = first_num
max_val = first_num
positive_count = 0
if first_num > 0:
    positive_count = 1
for i in range(2, n+1):
    num = int(input('Введите {i}-е число: '))
    total_sum += num
    if num > 0:
        positive_count += 1
    if num > max_val:
        max_val = num
print(f'Сумма: {total_sum}')
print(f'Кол-во положительных: {positive_count}')
print(f'Максимум: {max_val}')
