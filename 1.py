def evklid(sourse, base):
    res_code = ""
    while sourse > 0:
        res_code = str(sourse % base) + res_code
        sourse = sourse // base
    return res_code

num = int(input("Введите число: "))
r = int(input("Введите целевую систему счисления: "))

while (r != 2) and (r != 8):
    print("Система счисления не подходит")
    r = int(input("Введите систему счисления: "))

print(str(num) + " -> " + evklid(num, r))     