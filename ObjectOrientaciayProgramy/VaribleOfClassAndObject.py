from random import random
import string
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-^*'
class Robot:
    '''Представляет робота с именем.'''
    population = 0

    def __init__(self, name):
        '''Инитиализация данных..'''
        self.name = name
        print('(Inicyalization {0}...)'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''Загибаюсь...'''
        print('({0} daing...)'.format(self.name))

        Robot.population -=1

        if Robot.population == 0:
            print('Has been last(( ')
        else:
            print('Left {0:d} robots, who working.'.format(Robot.population))

    def sayHy(self):
        '''Приведствие робота,
        они эт могут'''
        print('Zig Hail Main furrer, my masters calling me {0}'.format(self.name))

    def howMany():
        '''Выводит количество работэу'''
        print('Now, we have {0} robots.'.format(Robot.population))

    howMany = staticmethod(howMany)

print('Добро пожаловать в империю зла!!!!!!'
      '\nМы можем строить с помощью роботов, но вам нужно:'
      '\n[1] - добавить робота; [2] - избавиться от последнего; '
      '\n[0] - узнать коллическво; [9] - выход')
x = ['добавить', 'призвать', 'add', '1']
y = ['убить', 'удалить', 'покорать', 'del', '2']
a = ['количество', 'quantity', 'сколько', '0']
b = ( )
n = ['выход', 'конец', 'end', 'exit', '9']
ne = ['нет', 'не', 'no', '0']
anton = True
while anton == True:
    z = input('Ваше решение гражданин!: ')
    if z in x:
        p = (int(random.choice(string.ascii_letters)), (random.choice(string.ascii_letters)),
             random.choice(string.ascii_letters),
             (random.choice(string.ascii_letters)), (random.choise(string.ascii_letters)))
        droid = Robot(p)
        droid.sayHy()
        Robot.howMany()
        b.expend(p)
        continue
    if z in y:
        droid.__del__(Robot.population[-1])
        del droid
        Robot.howMany()
        continue
    if z in a:
        Robot.howMany()
        print(b)
        continue
    if z in n:
        print('Ты точно хош выйти!?(( '
              '\n[9] - подтвердить; [0] - опровергнуть;')
        while True:
            ext = input()
            if ext in n:
                print('Ну ты иблан!!! Такую империю загнул!!')
                anton = False
                break
            if ext in ne:
                print('Фух... Продолжим!!!')
                break
            else:
                print('йа ни понеф короч')
        continue

    else:
        print('Йа нипанимаю нахуй!!')
        continue


print('We are use their, for the benifit of Holy Mother Russia!!! ')

print('We are killing their, becouse we will not need in waste materials')


