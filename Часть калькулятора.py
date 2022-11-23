ans = input('Для математичских действий(N), площадь(S), обьём(V). Напишите:')
if ans == 'N' or ans == 'n':
    qw = input('Введите 0 для простого калькулятора, @ для процентов, √ для корня:')
    while True:
        if qw == '0':
            calc = input("Введите математическое действие:\n")
            print("Ответ: " + str(eval(calc)))
            ex = input('Хотите продолжить?(Да/Нет):')
            if ex == 'Нет'or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break
            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()

        if qw == '@':
            b = input('Введите число:')
            a = input('Введите число процент которого хотите узнать:')
            c =float(a) / float(b) * 100
            print('ответ: ' +str(c))
            ex = input('Хотите продолжить?(Да/Нет):')
            if ex == 'Нет' or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break
            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()

        if qw == '√':
            import math

            num = ('Введите число корень которого хотите узнать:')
            sqrt = math.sqrt(num)
            print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))
while True:
    if ans == 'S' or ans == 's':
        import math
        R = float(input('Введите радиус круга:'))
        S = math.pi * R * R
        print('Площадь круга:', S)
        ex = input('Хотите продолжить?(Да/Нет):')
        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break
        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

    if ans == 'V' or ans == 'v':
        Vex = input('Обьём квадрата(С), или обьём параллелепипеда(P):')
        if Vex == 'P' or Vex == 'p':
            x = input('Введите высоту:')
            y = input('Введите ширину:')
            z = input('Введите глубину:')
            d = x * y
            t = z * d
            print('Результат' +str(t))
            ex = input('Хотите продолжить?(Да/Нет):')
            if ex == 'Нет' or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time

                time.sleep(5)
                break
            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()

    else:
        print('Ошибка, программа закроется через 5 секунд. отсчёт начался!!!')
        import time
        time.sleep(5)
