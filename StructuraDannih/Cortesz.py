print('Вспомни животных из зоопарка!:')
zoo = ('пингвин', 'жираф', 'собака', 'женщина')
print(zoo)
print('Кооличество их = ', len(zoo))
print('А какие рассы людей естбь на улице?:', end = ' ')
ne_zoo = ('мексиканец', 'русский', 'туркмен', 'украинец', 'еврей')
print(ne_zoo)
new_zoo = (ne_zoo, zoo)
print('Колличество клеток в зоопарке, кста ', len(zoo)+len(ne_zoo))
print('Представ, в городе Арийске, были бы в зоопарке: ', new_zoo)
print('Хоть многие машнят, что ', new_zoo[-1], ' животные,')
print('А с ', new_zoo[0][-1], ' например, так нельзя,')
print('Но тогда разместить в зоопарке прелагаю ', len(zoo) + len(ne_zoo) - 1)
# Шоб получить кортеж длиной 0, нужно написать a = ()
# А шоб длиной 1: a = (1, )