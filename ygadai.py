from random import randint
a = randint(1,10)
b = int(input('угадайте число от 1 до 10: '))
if b == a:
    print('правильно')
else:
    print('неправильно')