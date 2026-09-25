def run_task3():
    
    # просимо користувача ввести текст із цифр і літер
    text = input("Enter a text containing Latin letters and digits: ")
    
    # задаємо множину голосних літер за умовою
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    
    # задаємо множину приголосних літер
    consonants_set = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}
    
    # переводимо весь текст у малі літери, щоб не було плутанини
    text_lower = text.lower()
    
    # збираємо всі унікальні букви з тексту у множину
    letters_in_text = set()
    for char in text_lower:
        if char.isalpha():
            letters_in_text.add(char)
            
    # виводимо знайдені літери як множину на екран
    print("Unique letters found:", letters_in_text)
    
    # шукаємо голосні та приголосні через перетин множин
    found_vowels = letters_in_text.intersection(vowels_set)
    found_consonants = letters_in_text.intersection(consonants_set)
    
    # за умовою: якщо не можна зробити напряму з множиною 
    # перетворюємо її на список, а потім назад на множину для виведення
    vowels_list = list(found_vowels)
    consonants_list = list(found_consonants)
    
    # перетворюємо список назад у множину
    final_vowels = set(vowels_list)
    final_consonants = set(consonants_list)
    
    # рахуємо кількість
    vowels_count = len(final_vowels)
    consonants_count = len(final_consonants)
    
    # виводимо фінальні результати
    print("Vowels set:", final_vowels)
    print("Consonants set:", final_consonants)
    
    # порівнюємо, яких літер більше
    if vowels_count > consonants_count:
        print("Result: There are MORE VOWELS in the text.")
    elif consonants_count > vowels_count:
        print("Result: There are MORE CONSONANTS in the text.")
    else:
        print("Result: There is an EQUAL number of vowels and consonants.")
