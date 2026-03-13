import os


class FileManager:
    def __init__(self):
        self.file_list = []
        with open('file1.txt', 'a', encoding='utf-8') as f:
            self.file_list.append('file1.txt')
            f.close()
        with open('file2.txt', 'a', encoding='utf-8') as f:
            self.file_list.append('file2.txt')
            f.close()
        with open('file3.log', 'a', encoding='utf-8') as f:
            self.file_list.append('file3.log')
            f.close()

    def write(self, file, data):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(data)

    def read(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            result = f.read()
            print(result)

    def delete(self, file):
        index = self.file_list.index(file)
        del self.file_list[index]
        os.remove(file)

    def show(self):
        print()
        print('Оставшиеся файлы:')
        for file in self.file_list:
            print(file)


file_manager = FileManager()
for _ in range(4):
    data = input().split()
    if len(data) == 3:
        getattr(file_manager, 'write')(data[1], data[2])
    else:
        getattr(file_manager, data[0])(data[1])

file_manager.show()