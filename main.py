import random
import time
#na verxu importiruutsa 2 biblioteki random i vremya
#zdes spiski na angliskom i na ruskom
eng_words = ['Hi','Bye','Task', 'Programm']
ru_words = ['Привет','Пока','Задача', 'Программа']
#ochki = o
score = 0
#zdes nado vvesti rejim raboti trenajora chtobi proiti dalshe
mod = input("Выбери режим работы тренажера: 0 - добавить новые слова, 1 - тренироваться: \n")
#zdes kogda indeks moda = 0 i indeks moda = 1 togda simvol ne dastupni i nado vvesti pravelnie simvoli
while ((mod != '0') and (mod != '1')):
    mod = input("Недопустимый символ! Выбери 0 или 1. (0 - добавить новые слова, 1 - тренироваться) \n")
#zdes esli mod = 1 vvedotsa danni text vnezu
if mod == "1":
    print("Переведи как можно больше слов правильно! У тебя 10 попыток!")
    #zdes 10 raz number budet randomnim iz spiska eng_words i viveditsa danni tekst:Как переводится слово i kakoete slovo is eng_words
    for i in range(10):
        number = random.randint(0, len(eng_words))
        print("Как переводится слово: " + eng_words[number])
        #zdes esli predlojenie iz input budet slovom iz spiskaru_words to na ekran viveditsa:Отлично!!! i dobavitsa 1 ochko
        if input() == ru_words[number]:
            print("Отлично!!!")
            score += 1
        else:
            #ili viveditsa:Нет... Это слово i viveditsa pravelnoe slovo iz spiska ru_words
            print("Нет... Это слово - " + ru_words[number])
else:
    #ili zdes nado vvesti slovo na ruskom yazike v inpute
    word = input("Введите слово на русском языке: ")
    #zdes nado vvesti perevod etovo slovo
    translate = input("Введите перевод этого слова: ")
    #zdes esli slovo bolshe chem 0 i perevod bolshe chem 0 v spisok ru_word dobavitsa vvedonnoe slovo i v spisok eng_words dobavitsa perevod slovo i vvedotsa na ekran:Слово успешно добавлено!
    if len(word) > 0 and len(translate) > 0:
        ru_words.append(word)
        eng_words.append(translate)
        print("Слово успешно добавлено!")
