# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.


with open('task2.txt', encoding='utf-8') as f:
    s = f.read()
    k = list(s)
    k2 = k[::]
    cnt = 0
    for i in range(len(s) - 5):
        if k[i + 1: i + 6] == ['y', 't', 'h', 'o', 'n']:
            if k[i] == 'P':
                k2[i - cnt: i + 5 - cnt] = ["П", "и", "т", "о", "н"]
                del k2[i + 5 - cnt]
                cnt += 1
            elif k[i] == 'p':
                k2[i: i + 5 - cnt] = ["п", "и", "т", "о", "н"]
                del k2[i + 5 - cnt]
                cnt += 1

    f = open('task2_1.txt', 'w')
    f.write(''.join(k2))
    f.close()
    print(cnt)

