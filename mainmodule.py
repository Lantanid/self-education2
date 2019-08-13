import zigen

zigen.sayzighay()

if __name__ == 'zigen':
    print('sucking')
else:
    print('sucking too, but sucking with a twinge')
    print('Because a __name__ = ', __name__)

print('Версия: ', zigen._version_)