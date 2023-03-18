import sys

# вынесла в отдельную функцию "зачистку" текста от знаков препинания, знака абзаца и двойных пробелов
def clean_text(some_text):
    punc_marks = '''.,!?':;()-—"123456789*@#+='\\'{}[]|'''
    for i in punc_marks:
        if i in some_text:
            some_text = some_text.replace(i, '')
    some_text = some_text.replace('\n', '')
    some_text = some_text.replace('  ', ' ')
    return some_text
def count_unique():
    print("Введите текст: ")
    text = sys.stdin.readline()
    new_text = clean_text(text)
    word_list = list(new_text.split(sep=' '))
    unique = 0

    for i in range(0, len(word_list)):
        if word_list[i] not in word_list[(i + 1):len(word_list)] and word_list[i] not in word_list[0:i]:
            unique += 1
    print(f"В тексте {unique} уникальных слов(а).")

count_unique()