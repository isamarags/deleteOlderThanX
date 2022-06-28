############ DELETE OLDER THAN X ############
import os
import time
import shutil

current_time = time.time()
daysToDelete = 7
directory = 'C:/Users/06937762186/Downloads'

for dirpath,dirnames,filenames in os.walk(directory):

    for f in filenames:

        fileWithPath = os.path.abspath(os.path.join(dirpath, f))

        creation_time = os.path.getctime(fileWithPath)

        print("file available:",fileWithPath)

        #if (current_time - creation_time) // (24 * 3600) >= daysToDelete:
        if (current_time - creation_time) >= 10:
            os.unlink(fileWithPath)

            print('{} removed'.format(fileWithPath))
            print("\n")

        else:
            print('{} not removed'.format(fileWithPath))

    for f in dirnames:

        dirWithPath = os.path.abspath(os.path.join(dirpath, f))

        creation_time = os.path.getctime(dirWithPath)

        print("dir available:",dirWithPath)

        #if (current_time - creation_time) // (24 * 3600) >= daysToDelete:
        if (current_time - creation_time) >= 10:
            shutil.rmtree(dirWithPath)

            print('{} removed'.format(dirWithPath))

            print("\n")

        else:
            print('{} not removed'.format(dirWithPath))