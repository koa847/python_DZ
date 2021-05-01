import os

ROOT = os.path.dirname(__file__)
root_folder = 'my_project'
folder_name = ('settings', 'mainapp', 'adminapp', 'authapp')
paths =[os.path.join(root_folder, folder_name[i]) for i in range(0, len(folder_name))]

for folder_path in paths:
    os.makedirs(os.path.join(ROOT, folder_path), exist_ok=True)