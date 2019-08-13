import os
import time

source = ['C:\\MyDocuments']

target_dir = 'E:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
    print('Backup copy is successful create and put in ', target)
else:
    print('Backup copy is NOT some create!')