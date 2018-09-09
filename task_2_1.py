# # Написать программу сложения и умножения двух шестнадцатеричных чисел.


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


num1 = input("Введите первое шестнадцатеричное число: ")
x = int(num1, 16)

num2 = input("Введите второе шестнадцатеричное число: ")
y = int(num2, 16)

print(f"Результат сложения: {convert_base(x + y, to_base=16)}")
print(f"Результат умножения: {convert_base(x * y, to_base=16)}")
