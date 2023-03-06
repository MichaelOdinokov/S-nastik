from Omamodul import*
rus_dict=dict(zip(read_file('rus.txt'), read_file('est.txt'))) #создаёт словарь
est_dict=dict(zip(read_file('est.txt'), read_file('rus.txt')))

while True:
    print('Выберите действие:')
    print('1. Перевод с русского на эстонский')
    print('2. Перевод с эстонского на русский')
    print('3. Добавление нового слова в словарь') # ei töö..?
    print('4. Исправление перевода слова в словаре')# ei töö
    print('5. Проверка знания слов из словаря') # ei töö
    print('6. чтения данных из словаря') # ei töö
    print("7. write") # ei töö

    choice=int(input("Arv:"))

    if choice==1:
        word=input('Введите слово для перевода с русского на эстонский: ')
        translation=translate_rus_to_est(word, rus_dict)
        print(f'Перевод: {translation}')
    elif choice==2:
        word=input('Введите слово для перевода с эстонского на русский: ')
        translation=translate_est_to_rus(word, est_dict)
        print(f'Перевод: {translation}')
    elif choice==3:
        word=input('Введите новое слово: ')
        translation=input('Введите перевод слова: ')
        add_word_to_dict
    elif choice==4:
        edit_translation_in_dict
    elif choice==5:
        test_word_knowledge
    elif choice==6:
        read_file
    elif choice==7:
        write_file
    

