import re
import os

def persing_file (file):
    pattern = re.compile(r'(^.+)\s-\s-\s\[(.+)]\s"(\w+[A-Z])\s(/\w+/\w+)\s.+"\s(\d+)\s(\d+)\s')
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            r = pattern.finditer(line)
            for i in r:
                result.append((i.group(1), i.group(2), i.group(3), i.group(4), i.group(5), i.group(6)))
    return result

if __name__ == '__main__':
    file = 'nginx_logs.txt'
    path_file = os.path.abspath(file)
    f_list = persing_file(path_file)
    for str in f_list:
        print(str)

