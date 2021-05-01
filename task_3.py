import os
from shutil import copy

ROOT = os.path.join(os.path.dirname(__file__), 'my_project')
path_temp = os.path.join(ROOT, 'templates')


try: os.mkdir(path_temp)
except FileExistsError: pass

for root, folders, files in os.walk(ROOT):

    if root.count('templates'):

        for folder in folders:
            try: os.mkdir(os.path.join(path_temp, folder))
            except FileExistsError: pass

        for file in files:
            path_folder = os.path.join(path_temp, os.path.basename(root))
            try:
                copy(os.path.join(root, file), path_folder)
            except IOError: pass