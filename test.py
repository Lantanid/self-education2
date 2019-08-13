def opis():
      '''
    Эта программа был из тех, кто находит наибольшее число кароч, из чисел
    что ты ща можешь ввести...
    ц'''
def printMax(x):
    z = 0
    i = x[0]
    for init in x:
        if i < init:
            i = init
        elif x[0] > init:
            continue
        else:
            z = z + 1
    if z == len(x):
        print('Все числа равны, чё ты лепишь!!')
    else:
        print('Наибольшее число ', i)

def isFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        print("Введи нормально!!! Я не понимаю нахуй!!!")
        return False

def inputFloatNumber():
    print('Введи число[0 - кончить]:', end=' ')
    a = input()
    while not isFloat(a):
        print('Введи снова![0 - кончить]:', end=' ')
        a = input()
    return a

def vvod():
    b = []
    while True:
        a = inputFloatNumber()
        a = int(a)
        if a != 0:
            b.append(a)
        else:
            break
    return b

print('Дарова, эта супер прога сделает все твои жэлания!!!')
print('Шоб начать арбайтен, зокончить, иль узнать что прога делает, спроси, или дай знац...')
while True:
    print('Подсказка:[1 - показац кто сдес батя; 2 - обиснить не возможно; 0 - покинуть заведение; F - поуважать ветеринаров!')
    ad = input('Вводим: ')
    if ad == '1':
        print('Шоб прикратить вводить, тапни 0. \nПогнали нахуй!:')
        b = vvod()
        printMax(b)
        continue
    if ad == '2':
        print(opis.__doc__)
        continue
    if ad == '0':
        break
    else:
        print('Я не понимаю нахуй!!!')
print('Досвидулькин!((')