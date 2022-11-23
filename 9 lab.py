import random
#импортирую библиотеку лога и провожу её стандартную настройку
import logging
logging.basicConfig(filename="3thLog.log", 
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%H: %M: %S',
                    level=logging.DEBUG)
#создаю функцию проверки на ошибки ввода
def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        logging.error('Неверный ввод!')
        return -1
    return n
N = - 1
while N == -1:
    N = int(input('Начало диапазона возможных значений = 1, введите конец диапазона возможных значений:\n'))
    N = errorCheck(N)
logging.info(f'Пользователь ввёл значение {N} как конец диапазона возможных значений')

k = -1
while k == -1:
    k = int(input('Введите количество попыток:\n'))
    k = errorCheck(k)
logging.info(f'Пользователь ввёд число {k} как количество попыток')

chislo = random.randrange(1,N+1,1)
logging.info(f'Загадано число {chislo}')
turn =1
for i in range(k):
    num = -1
    while num == -1:
        num = int(input(f'Попробуйте угадать число от 1 до {N}:\n'))
        num = errorCheck(num)
    logging.info(f'Пользователь ввёл число {num} как вариант отгадки')
    if num > chislo:
        print('Ваше число больше загаданного\n')
        logging.info('Пользователь не отгадал число')
    elif num < chislo:
        print('Ваше число меньше загаданного\n')
        logging.info('Пользователь не отгадал число')
    elif num == chislo:
        print('Невероятно, вы угадали, вашей интуиции позавидовал бы каждый!\n')
        logging.info('Пользователь отгадал число')
        break
    logging.info(f'Пользователь использовал {turn} из {k} попыток')
    turn +=1
