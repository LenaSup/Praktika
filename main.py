def calculator(s):
    sl = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
          'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 12, 'четырнадцать': 14, 'пятнадцать': 15,
          'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30,
          'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90,}
    sl_z = {'скобкаоткрывается': '(', 'скобказакрывается': ')', 'плюс': '+', 'минус': '-', 'умножитьна': '*'}

    s = s.replace('скобка открывается', 'скобкаоткрывается')
    s = s.replace('скобка закрывается', 'скобказакрывается')
    s = s.replace('умножить на', 'умножитьна')
    s = s.split()

    xyz = [0]
    k = 0
    for i in s:
        if i in sl:
            xyz[k] += sl[i]
        elif xyz[-1] != 0:
            xyz.append(0)
            k += 1

    k = 0
    fl = True
    for i in range(len(s)):
        if s[i] in sl_z:
            fl = True
            s[i] = sl_z[s[i]]
        elif fl:
            fl = False
            s[i] = str(xyz[k])
            k += 1

#    out = calc_bez_eval(s)
    s = ' '.join(s)
    out = eval(s)

#   -----------------------------------------
    if out > 100 or out < -100:
        return 'Результат выходит за пределы допустимых значений'
    if abs(out) in sl.values():
        if out >= 0:
            return list(sl.keys())[list(sl.values()).index(out)]
        else:
            out = abs(out)
            return 'минус ' + list(sl.keys())[list(sl.values()).index(out)]
    if out >= 0:
        return (list(sl.keys())[list(sl.values()).index(out // 10 * 10)] + ' ' +
                list(sl.keys())[list(sl.values()).index(out % 10)])
    else:
        out = abs(out)
        return 'минус ' + (list(sl.keys())[list(sl.values()).index(out // 10 * 10)] + ' ' +
                list(sl.keys())[list(sl.values()).index(out % 10)])


def calc_bez_eval(s):   # :(
    k = 0
    while s[k] != ')':
        if s[k] == '(':
            calc_bez_eval(s[k + 1:])
            while '*' in s:
                i = '*'.index(s)
                s = s[:i - 1] + int(s[i - 1]) * int(s[i + 1]) + s[i + 2:]
        k += 1


#   4 5 3
print(calculator('пять плюс два умножить на три минус один'))