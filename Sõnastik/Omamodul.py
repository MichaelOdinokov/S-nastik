from random import*

# Основная функция программы
def main():
    # Чтение данных из файлов
    rus_dict=dict(zip(read_file('rus.txt'), read_file('est.txt'))) #создаёт словарь

    while True:
        print('Выберите действие:')
        print('1. Перевод с русского на эстонский')
        print('2. Перевод с эстонского на русский')
        print('3. Добавление нового слова в словарь')
        print('4. Исправление перевода слова в словаре')
        print('5. Проверка знания слов из словаря')
        print('6. Выход')
        choice=input().strip()

        if choice==1:
            word = input('Введите слово для перевода: ')
            translation=translate_rus_to_est(word, rus_dict)
            print(f'Перевод: {translation}')
        elif choice==2:
            word=input('Введите слово для перевода: ')
            translation=translate_rus_to_est(word, rus_dict)
            print(f'Перевод: {translation}')
        elif choice==3:
            add_word_to_dict
        elif choice==4:
            edit_translation_in_dict
        elif choice==5:
            test_word_knowledge
        

# Функция для чтения данных из файла и сохранения их в список
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        data=[line.strip() for line in f]#strip() удаляет любые пробельные символы
    return data

# Функция для записи данных из списка в файл
def write_file(data, filename):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for item in data:
            f.write(item + '\n')

# Функция для перевода слова с русского на эстонский
def translate_rus_to_est(word, dictionary):
    return dictionary.get(word, 'Слово не найдено в словаре')#Если ключ word в словаре то возвращает значение из словаря

# Функция для добавления слова в словарь
def add_word_to_dict(dictionary):
    word=input('Введите новое слово: ')
    translation=input('Введите перевод слова: ')
    dictionary[word]=translation
    return dictionary

# Функция для исправления перевода слова в словаре
def edit_translation_in_dict(word, dictionary):
    if word in dictionary:
        new_translation=input(f'Введите новый перевод для слова "{word}": ')
        dictionary[word]=new_translation
    else:
        print('Слово не найдено в словаре')

# Функция для проверки знания слов из словаря
def test_word_knowledge(dictionary):
    words=list(dictionary.keys())#Эта функция создает список, содержащий все ключи (слова) из словаря.
    random.shuffle(words)#перемешивает элементы списка words в случайном порядке. 
    correct=0
    total=len(words)
    for word in words:
        print(f'Переведите слово "{word}"')
        answer=input().strip()
        if answer==dictionary[word]:
            print('Правильно!')
            correct+=1
        else:
            print(f'Неправильно. Правильный ответ: {dictionary[word]}')
    percentage_correct=(correct/total)*100
    print(f'Вы ответили правильно на {percentage_correct}% вопросов')




