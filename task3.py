# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from fileinput import close

import numpy
import numpy as np


with open('task3.txt', encoding='utf-8') as f:
    s = f.read()
    e = list(s)
    while ',' in e:
        e.remove(',')
    while '.' in e:
        e.remove('.')

    a = np.array(''.join(e).split())
    for i in range(len(a)):
        a[i] = a[i].lower()
    k = np.unique(a, return_counts=True)
    d = {}

    b = k[0]
    c = k[1]
    for i in range(len(b)):
        d[str(b[i])] = str(c[i])

    keys = sorted(d, key=str.lower)
    file = open('task3_1.txt', 'w', encoding='utf-8')
    for i in keys:
        file.write(f'{i}: {d[i]} \n')
    close()