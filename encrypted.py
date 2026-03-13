with open('secret.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Secret World')

key = int(input())

with open('secret.txt', 'r', encoding='utf-8') as f1, open('encrypted.txt', 'a', encoding='utf-8') as f2:
    data = f1.read().strip()
    for char in data:
        f2.write(str(ord(char) ^ key))

with open('encrypted.txt', 'r', encoding='utf-8') as file:
    result = ''
    data = file.read()
    for char in data:
        result += str(chr(int(char) ^ key))
    print(result)