import random

# my_list = [randint(1, 100) for _ in range(10)]

my_list = []
for i in range(100):
    my_list.append(random.randint(1, 100))

print("Lista antes da ordenação", my_list)

n = len(my_list)
for i in range(n):
    for j in range(n - 1):
        if my_list[j] > my_list[j + 1]:
            # Swap elements
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print("Lista depois", my_list)
