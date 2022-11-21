ans = input('Для математичских действий(N), площадь(S), обьём(V). Напишите:')
if ans == 'N':
    Qw = input('Введите 0 для простого калькулятора, @ для процентов:')
    while True:
        if Qw == '0':
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

        if Qw == '@':
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