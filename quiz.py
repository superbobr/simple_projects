with open('quiz.txt', 'w+', encoding='utf-8') as file:
    file.write('Столица Франции? Париж' + '\n')
    file.write('2 + 2 * 2? 6' + '\n')
    file.write('Самая длинная река в мире? Амазонка' + '\n')
    file.seek(0)
    result = 0
    data = file.readlines()

    for line in data:
        temp = line.split('?')
        answer = input(f'{temp[0]}?\n')
        if answer.strip().lower() == temp[1].strip().lower():
            result += 1

    print(f'Ваш счет: {result}')