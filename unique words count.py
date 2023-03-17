
text = input(f"Введите текст: ")
punc_marks = '''.,!?':;()-—"123456789*@#+='\\'{}[]|'''

# удаляем из текста все, что мешает подсчету слов - знаки препинания и двойные пробелы
for i in punc_marks:
    if i in text:
        text = text.replace(i, '')
text = text.replace('  ', ' ')

# создаем список всех слов в тексте и словарь из них же, где значение это счетчик встречаемости (по дефолту 0)
word_list = list(text.split(sep=' '))
text_dict = dict.fromkeys(word_list, 0)



# в значениях словаря подсчитываем встречаемость каждого слова
for i in word_list:
    text_dict[i] += 1

# считаем сколько слов в словаре встречаются по одному разу
count_unique = 0
for value in text_dict.values():
    if value == 1:
        count_unique +=1


print(f"В тексте {count_unique} уникальных слов(а).")


