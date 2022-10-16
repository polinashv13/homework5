num = int(input("Введите число: "))
r = int(input("Введите целевую систему счисления: "))
while (r != 2) and (r != 8):
    print("Система счисления не подходит")
    r = r = int(input("Введите систему счисления: "))
if r == 2:
    print(str(num) + " -> " + bin(num)[2:])
else:
    print(str(num) + " -> " + oct(num)[2:])     