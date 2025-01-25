# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

with open('task5.txt', encoding='utf-8') as f:
    e = list(f.read())
    while ',' in e:
        e.remove(',')
    while '.' in e:
        e.remove('.')
    while '!' in e:
        e.remove('!')
    a = ''.join(e).split()

    ma = ''
    for i in a:
        if len(i) > len(ma):
            ma = i
fi = open('task5_1.txt', 'w', encoding='utf-8')
fi.write(f'Самое длинное слово: {ma} \n')
fi.write(f'Его длина: {len(ma)}')
