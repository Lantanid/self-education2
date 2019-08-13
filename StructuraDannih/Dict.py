ad = { 'Swaroop'    :  'swaroop@swaroopch.com',
       'Larry'      :  'larry@wall.org',
       'Matsumoto'  :  'matz@zuby-lang.com',
       'Spammer'    :  'soammer@hotmail.com'}
#Задаёца кароч пара: ключ(д.б. простой и неизменный):Значение(пох какое), и причём в фигурных скабках, пары через запятую.
print('Swaroop', ad['Swaroop'])
#можна значит выводить вот так значение
del ad['Spammer']
#А так удалять элемент, через ключ
print('\nВ адресной книге {0} контактов\n'.format(len(ad)))
for name, adress in ad.items():
    print('Контакт {0} с адресом {1}'.format(name, adress))
#в циклах так мож работать
ad['Doiky'] = 'sosiski@doiki.com'
#так добавлять новую пару
if 'Doiky' in ad:
    print('\nАдрес Doiky ', ad['Doiky'])
#и даж ветвление ипашить
#!!!!Проверить есть ли значение м с пом оператора in.