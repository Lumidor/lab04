n = int(input("Введите количество чисел n (n >= 0): "))
count = 0
total_sum = 0
for i in range(n):
    num = int(input("Введите число: "))
    if num < 0:
        count += 1
        total_sum += num
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
