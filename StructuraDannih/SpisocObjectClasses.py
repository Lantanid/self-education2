shoplist = ['Фалоиметатор', 'Аннальные шарики', 'Украинскую майку', 'Кило тротила', 'Батон']

print('Я долже сделац ', len(shoplist), ' покупки')

print('Покупки: ', end = ' ')

for item in shoplist:
    print(item, end = ' ')

print('\nТак же нужно купить Трусики Рины Поленковой')
shoplist.append('Трусики РП')
print('Теперь набор юнного любителя России таков: ', shoplist)

print('От-сартир-ую-ка я список!')
shoplist.sort()
print('после сортирфикации список выглядае: ', shoplist)

print('Первое, что нужно, это ', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Но у твоей мамки уже есть ', olditem)
print('Так что мой список теперь: ', shoplist)