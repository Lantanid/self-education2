from zigen import sayzighay, _version_               # м ищё записать, как from zigen import *  - но эт импортирует все имена, акрымя _version_, т.к. оно нач. с подчеркивания

sayzighay()

if __name__ == 'zigen':
    print('Sucking')
else:
    print('Sucking too, but sucking with a twinge')
    print('Because a __name__ = ', __name__)
print('Версия ', _version_)