text = '''Это первая строка для анализа.
А это уже вторая строка.
И, наконец, третья.'''

with open('text_for_analysis.txt', 'w+', encoding='utf-8') as file:
    file.write(text)
    file.seek(0)
    data = file.readlines()
    rows = len(data)
    words = 0
    chars = 0
    for line in data:
        words += len(line.split())
        chars += len(line)

print(
f'''Символов: {chars}
Слов: {words}
Строк: {rows}''')