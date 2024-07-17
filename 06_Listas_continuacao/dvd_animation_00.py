import os
import time

screen_size_width = 8
screen_size_height = 6

screen = []
for y in range(screen_size_height):
    for x in range(screen_size_width):
        screen[x][y] = "."

cur_x = 0
cur_y = 0

move_x = 1
move_y = 1

os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela

while True:
    screen[cur_x][cur_y] = "A"

    for line in range(screen_size_height):
        print(" ".join(screen[line]))

    time.sleep(0.5)  # Espera meio segundo (500ms)
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela

    screen[cur_x][cur_y] = "."
    if (cur_x + move_x) < 0:  # Saindo pela esquerda
        move_x *= -1
    if (cur_y + move_y) < 0:  # Saindo pelo topo
        move_y *= -1

    if len(screen) == cur_x + move_x:  # Saindo pela direita
        move_x *= -1
    if len(screen[cur_x]) == cur_y + move_y:  # Saindo pela base
        move_y *= -1

    cur_x = cur_x + move_x
    cur_y = cur_y + move_y
