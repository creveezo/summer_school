import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
cur_attempt = 1
attempts_left = 6
win = False

with open(f"dict_wide.txt", "r", encoding="UTF-8") as file:
    wide = file.read().split("\n")

with open(f'dict_narrow.txt', 'r') as f:
    narrow = f.read().split("\n")
    game_word = random.choice(narrow).lower()


def AllowCheck(word):
    SymbAllowed = True
    for i in list(word.lower()):
        if i not in alphabet:
            SymbAllowed = False
            break
    if SymbAllowed == False:
        print("Недопустимый символ в слове. Попробуйте снова")
    return SymbAllowed


def LenCheck(word):
    if len(word) < 5:
        print("Слово слишком короткое, попробуйте снова")
        return False
    if len(word) > 5:
        print("Слово слишком длинное, попробуйте снова")
        return False
    return True


def user_input():
    return normal_word()


def normal_word():
    user = input("Ваше слово: ").lower().strip()
    Allow = AllowCheck(user)
    Length = LenCheck(user)
    if Allow == False or Length == False:
        return normal_word()
    if user not in wide:
        print("Данное слово не найдено. Попробуйте снова")
        return normal_word()
    return user


def letters(user, guess):
    d_game = {}
    list = []
    for i in range(5):
        if user[i] == guess[i]:
            list.append([user[i], "green"])
        elif user[i] not in guess:
            list.append([user[i], "gray"])
        elif user.count(user[i]) <= guess.count(user[i]):
            list.append([user[i], "yellow"])
        else:
            list.append([user[i], "0"])
            d_game.setdefault(user[i], 0)
    for let, count in d_game.items():
        d_game[let] = guess.count(let) - list.count([let, "green"])
    for i in list:
        if i[1] == "green":
            print(f'{i[0]} стоит на правильном месте')
        elif i[1] == "gray":
            print(f'{i[0]} отсутствует в слове')
        elif i[1] == "yellow":
            print(f'{i[0]} есть, но стоит не там')
        else:
            if int(d_game[i[0]]) > 0:
                d_game[i[0]] -= 1
                print(f'{i[0]} есть, но стоит не там')
            else:
                print(f'{i[0]} отсутствует в слове')

while attempts_left > 0:
    print(f"Попытка {cur_attempt}")
    user_word = normal_word()
    attempts_left -= 1
    cur_attempt += 1
    if user_word == game_word:
        print("Поздравляем, вы выиграли!")
        win = True
        break
    letters(user_word, game_word)

if not win:
    print(f"К сожалению, вы проиграли. Загаданное слово: {game_word}")
