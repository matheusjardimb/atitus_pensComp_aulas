import os
import time

screen_size_width = 21
screen_size_height = 13
total_pixels = screen_size_width * screen_size_height

screen = [[" " for x in range(screen_size_width)] for y in range(screen_size_height)]

cur_x, cur_y = 0, 0
move_x, move_y = 1, 1

hit_count = 0

os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela

while True:
    screen[cur_x][cur_y] = "0"

    total_filled = 0
    print("-" * (screen_size_width + 2))
    for line in range(screen_size_height):
        row = "".join(screen[line])
        total_filled += row.count("0") + row.count(".")
        print("|" + row + "|")
    print("-" * (screen_size_width + 2))
    print("Percentual preenchido:", (total_filled / total_pixels) * 100, "%")
    print("Número de vezes que atingiu uma parede:", hit_count)

    time.sleep(0.5)  # Espera meio segundo (500ms)
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela

    init_move_x = move_x
    init_move_y = move_y

    screen[cur_x][cur_y] = "."
    if (cur_x + move_x) < 0:  # Saindo pela esquerda
        move_x *= -1
    if (cur_y + move_y) < 0:  # Saindo pelo topo
        move_y *= -1

    if len(screen) == cur_x + move_x:  # Saindo pela direita
        move_x *= -1
    if len(screen[cur_x]) == cur_y + move_y:  # Saindo pela base
        move_y *= -1

    if init_move_x != move_x or init_move_y != move_y:
        hit_count += 1

    cur_x = cur_x + move_x
    cur_y = cur_y + move_y
