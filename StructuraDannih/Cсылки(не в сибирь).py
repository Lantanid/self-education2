print('Easy cutting')
shoplist = ['ogurki', 'pomidory', 'annal oil', 'artifical vagine']
mylist = shoplist

del shoplist[0]
print('Shoplist: ', shoplist)
print('MyList: ', mylist)

print('\nCopy with need full cutting (virezka)')
mylist = shoplist[:]
del mylist[0]

print('Shoplist: ', shoplist)
print('MyList: ', mylist)

