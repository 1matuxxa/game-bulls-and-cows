import random 

def main_game_medium():
    mechanical_digits = ""
    while len(mechanical_digits) != 4:
        random_digit = str(random.randint(0,9))
        if random_digit not in mechanical_digits:
            mechanical_digits += str(random_digit)
    print(mechanical_digits)
    count = 0

    while True:
        flag = True
        cows = 0
        bulls =  0
        user_guess = str(input('введите ваше четырехзначное число:'))
        if len(user_guess) != 4:
            print('число должно состоять из 4 элементов')
            continue
        for i in user_guess:
            if user_guess.count(i) != 1:
                flag = False
                break
        if flag == False:
            if count == 0: count += 0
            else: count -= 0
            print(f'число должно быть неповторяющимся, количество ваших попыток: {count}')
            continue
        if flag:
            for i in range(4):
                if user_guess[i] == (mechanical_digits)[i]:
                    bulls += 1
                if user_guess[i] in (mechanical_digits) and user_guess[i] != mechanical_digits[i]:
                    cows += 1
            count += 1
            if count == 10:
                return print('вы исчерпали количество попыток, хотите попробовать еще раз?')
            if bulls != 4:
                print(f'коровы: {cows}')
                print(f'быки: {bulls}')
                print(f'попыток: {count}')
            else:
                return print(f'вы выйграли!!! ваше количество попыток: {count}')

def main_game_easy():
    mechanical_digits = ""
    while len(mechanical_digits) != 3:
        random_digit = str(random.randint(0,9))
        if random_digit not in mechanical_digits:
            mechanical_digits += str(random_digit)
    print(mechanical_digits)
    count = 0

    while True:
        flag = True
        cows = 0
        bulls =  0
        user_guess = str(input('введите ваше трехзначное число:'))
        if len(user_guess) != 3:
            print('число должно состоять из 3 элементов')
            continue
        for i in user_guess:
            if user_guess.count(i) != 1:
                flag = False
                break
        if flag == False:
            if count == 0: count += 0
            else: count -= 0
            print(f'число должно быть неповторяющимся, количество ваших попыток: {count}')
            continue
        if flag:
            for i in range(3):
                if user_guess[i] == (mechanical_digits)[i]:
                    bulls += 1
                if user_guess[i] in (mechanical_digits) and user_guess[i] != mechanical_digits[i]:
                    cows += 1
            count += 1
            if count == 15:
                return print('вы исчерпали количество попыток, хотите попробовать еще раз?')
            if bulls != 3:
                print(f'коровы: {cows}')
                print(f'быки: {bulls}')
                print(f'попыток: {count}')
            else:
                return print(f'вы выйграли!!! ваше количество попыток: {count}')

def main_game_hard():
    mechanical_digits = ""
    while len(mechanical_digits) != 5:
        random_digit = str(random.randint(0,9))
        if random_digit not in mechanical_digits:
            mechanical_digits += str(random_digit)
    print(mechanical_digits)
    count = 0
    while True:
            m = []
            flag = True
            cows = 0
            bulls =  0
            user_guess = str(input('введите ваше пятизначное число:'))
            if len(user_guess) != 5:
                print('число должно состоять из 5 элементов')
                continue
            for i in user_guess:
                if user_guess.count(i) != 1:
                    flag = False
                    break
            if flag == False:
                if count == 0: count += 0
                else: count += 0
                print(f'число должно быть неповторяющимся, количество ваших попыток: {count}')
                continue
            if flag:
                for i in range(5):
                    if user_guess[i] == (mechanical_digits)[i]:
                        bulls += 1
                    if user_guess[i] in (mechanical_digits) and user_guess[i] != mechanical_digits[i]:
                        cows += 1
                count += 1
                if count == 7:
                    return print('вы исчерпали количество попыток, хотите попробовать еще раз?')
                if bulls != 5:
                    print(f'коровы: {cows}')
                    print(f'быки: {bulls}')
                    print(f'попыток: {count}')
                else:
                    return print(f'вы выйграли!!! ваше количество попыток: {count}')

def change_the_difficulty():
    user_changer = input('введите уровень сложности:')
    if user_changer == 'легкая':
        main_game_easy()
    if user_changer == 'средняя':
        main_game_medium()
    if user_changer == 'сложная':
        main_game_hard()
change_the_difficulty()