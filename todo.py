class Todo:
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)

    def show(self):
        for number, task in enumerate(self.todo_list, start=1):
            print(f'{number}. {task}')

    def delete(self, task_number):
        del self.todo_list[int(task_number) - 1]


todo = Todo()

for _ in range(5):
    command = input().split(maxsplit=1)
    if command[0] == 'show':
        todo.show()
    else:
        getattr(todo, command[0])(command[1])

