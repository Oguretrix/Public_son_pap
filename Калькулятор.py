what = input('Что делаем?(+,-,*,/,**):')

a = float(input('Введи первое число:'))
b = float(input('Введи второе число:'))

if what == '+':
    c = a + b
    print('Результат: ' + str(c))

elif what == '-':
    c = a - b
    print('Результат: ' + str(c))

elif what == '*':
    c = a * b
    print('Результат: ' + str(c))

elif what == '/':
    c = a / b
    print('Результат: ' + str(c))

elif what == '**':
    c = a ** b
    print('Результат: ' + str(c))
else:
    print('Выбранно неправильное действие!')

print('Нажмите Enter чтобы начать закрытие программы!!!')
input()
print('Подождите 10 секунд чтобы программа закрылась сама. Отсчёт начался!!!')
import time
time.sleep(10)
