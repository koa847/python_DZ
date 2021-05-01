import os
import json
# Задача №4
folder = 'my_project'
ROOT = os.path.dirname(__file__)
path_folder = os.path.join(ROOT, folder)

sum_file = {0:0}
sum_file.update({10**(i+1): 0 for i in range(0, 7)})

for root, _, files in os.walk(path_folder):
    for f in files:
        f_size = os.stat(os.path.join(root, f)).st_size
        if f_size == 0:
            sum_file.update({0: sum_file[0] + 1})
        else:
            sum_file.update({10**(i+1): sum_file[10**(i+1)]+1 for i in range(0, 7) if 10**i < f_size <= 10**(i+1)})
#Задача № 5
for el in sum_file:
    sum_file[el] = (sum_file[el], [])

for root, _, files in os.walk(path_folder):
    for f in files:
        f_size = os.stat(os.path.join(root, f)).st_size
        filetype = os.path.splitext(f)[1]
        if f_size == 0:
            if filetype not in sum_file[0][1] and filetype:
                sum_file[0][1].append(filetype)
        else:
            for i in range(0, 7):
                if 10**i < f_size <= 10**(i+1) and filetype not in sum_file[10**(i+1)][1] and filetype:
                    sum_file[10 ** (i + 1)][1].append(filetype)

file_name = folder + '_summary.json'

with open(file_name, 'w', encoding="utf-8") as f:
    json.dump(sum_file, f)


print(sum_file)