from random import*

# Функция для чтения данных из файла и сохранения их в список
def read_file(filename):
    f=open("est.txt", 'r', encoding='utf-8-sig')
    print(f.read())
    print()
    f=open("rus.txt", 'r', encoding='utf-8-sig')
    print(f.read())
    f.close()
# Функция для записи данных из списка в файл
def write_file(data,):
    with open("est.txt", 'w', encoding='utf-8-sig') as f:
        for item in data:
            f.write(item + '\n')

def translate_est_to_rus(word, dictionary):
     return dictionary.get(word, 'Слово не найдено в словаре')# Если ключ word в словаре то возвращает значение из словаря


# Функция для перевода слова с русского на эстонский
def translate_rus_to_est(word, dictionary):
    return dictionary.get(word, 'Слово не найдено в словаре')#Если ключ word в словаре то возвращает значение из словаря

# Функция для добавления слова в словарь
def add_word_to_dict(dictionary, word, translation):
    dictionary[word]=translation
    dictionary[word].append("est.txt")
    translation.append("rus.txt")
    return dictionary

# Функция для исправления перевода слова в словаре
def edit_translation_in_dict():
    with open("rus.txt","w", encoding='utf-8-sig'):
        wordrus=input("Введите занова слово на русском:")        
    with open("est.txt","w", encoding='utf-8-sig'):
        word=input("Введите занова слово на эстонском:")

# Функция для проверки знания слов из словаря
"""def test_word_knowledge(dictionary)->str:    
    words=list(dictionary.keys())#Эта функция создает список, содержащий все ключи (слова) из словаря.
    random.shuffle(words)#перемешивает элементы списка words в случайном порядке. 
    correct=0
    total=len(words)
    for word in words:
        print(f'Переведите слово: {word}-')
        answer=input().strip()
        if answer==dictionary[word]:
            print('Правильно!')
            correct+=1
        else:
            print(f'Неправильно. Правильный ответ: {dictionary[word]}')
    percentage_correct=(correct/total)*100
print(f'Вы ответили правильно на {percentage_correct}% вопросов')
"""

def test_word_knowledge(rus:list, est: list)->str:
    kokku=int(input("Mitu küsimust?"))
    for i in range(kokku):
        järjend=choice=([rus, est])
        sõna=choice(järjend)
        print(f"{sõna}")
        tõlke=input()
        if sõna in rus:
            i=rus.index(sõna)
            tõlke_kontroll=est[i]
        elif sõna in est:
            i=est.index(sõna)
            tõlke_kontroll=rus[i]
        if tõlke==tõlke_kontroll:
            p+=1
            print("Õige")
        else:
            print("Vale")
        p=5
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else:
        hinne="Väga halb"
    return hinne
