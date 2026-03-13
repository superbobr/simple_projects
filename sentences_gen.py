import random


subjects = ["Кошка", "Собака", "Птица"]
verbs = ["сидит", "бежит", "летит"]
objects = ["на дереве", "по дороге", "в небе"]

lsts = [subjects, verbs, objects]

random.seed(int(input()))
sentences = int(input())

for _ in range(sentences):
    print(" ".join(random.choice(lst) for lst in lsts) + ".")