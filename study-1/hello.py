Number1 = 0
Number2 = 0
count = 0
while float(count) == 0:
    count = input("Введите кол-во чисел ")
znak = input("Введите знак:" + "\n 1.+" + "\n 2.-" + "\n 3.*" + "\n 4./ " )
if float(znak) == 1:
    while float(count) != 0:
        Number1 = input("Введите число ")
        Number2 += float(Number1)
        count = float(count) - 1
if float(znak) == 2:
    Number1 = input("Введите число ")
    Number2 += float(Number1)
    while float(count) != 1:
        Number1 = input("Введите число ")
        Number2 -= float(Number1)
        count = float(count) - 1
if float(znak) == 3:
    Number1 = input("Введите число ")
    Number2 += float(Number1)
    while float(count) != 1:
        Number1 = input("Введите число ")
        Number2 *= float(Number1)
        count = float(count) - 1
if float(znak) == 4:
    Number1 = input("Введите число ")
    Number2 += float(Number1)
    while float(count) != 1:
        Number1 = input("Введите число ")
        while (float(Number1) == 0):
            Number1 = input("На ноль делить нельзя ")
        Number2 /= float(Number1)
        count = float(count) - 1
print("Результат ", '{0:.2f}'.format(float(Number2)))