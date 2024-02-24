from random import randint
a = randint(1,100)
b = int(input('угадайте число от 1 до 10: '))
while b != a:
    print('неправильно, повторите попытку')
    if a < b:
        print('загаданое число меньше')
    else:
        print('загаданое число больше')
    b = int(input('угадайте число от 1 до 10: '))
print('верно, вы угадали')