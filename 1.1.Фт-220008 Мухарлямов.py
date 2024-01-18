a = int(input('Введите число a — '))
b = int(input('Введите число b — '))
maxn = 0
minn = 0
summ = a + b
raz = a - b
mult = a * b
avg = (a + b) / 2
quo = round(a/b, 2)
if (a > 0) and (b > 0):
    a = a
    b = b
    if a > b:
        maxn = a
        minn = b
    elif a < b:
        maxn = b
        minn = a
    elif a == b:
        maxn = a = b
        minn = a = b

if (a < 0) and (b < 0):
    a = -a
    b = -b
    if a > b:
        maxn = a
        minn = b
    elif a < b:
        maxn = b
        minn = a
    elif a == b:
        maxn = a = b
        minn = a = b
if (a > 0) and (b < 0):
    a = a
    b = -b
    if a > b:
        maxn = a
        minn = b
    elif a < b:
        maxn = b
        minn = a
    elif a == b:
        maxn = a = b
        minn = a = b
if (a < 0) and (b > 0):
    a = -a
    b = b
    if a > b:
        maxn = a
        minn = b
    elif a < b:
        maxn = b
        minn = a
    elif a == b:
        maxn = a = b
        minn = a = b
print('Сумма = ' + str(summ))
print('Разность = ' + str(raz))
print('Произведение  = ' + str(mult))
print('Среднее арифметическое = ' + str(avg))
print('Разность max и min = ' + str(maxn-minn))
print('Частное = ' + str(quo))