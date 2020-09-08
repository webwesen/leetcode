#!/usr/bin/env python3

# n = 4
# s = "1B 2C,2D 4D"
# t = "2B 2D 3D 4D 4A"
n = 26
s = "1A 2A,12A 12A"
t = "12A"


def battleship(n, s, t):

    print(F'{n} | {s} | {t}')
    sunk = hit = 0
    ship_coordinates = list()

    ships = s.split(",")
    hits = set(t.split(" "))

    for i in range(len(ships)):
        ships[i] = ships[i].split(" ")
        top_left = ships[i][0]
        bottom_right = ships[i][1]
        temp_ship_coordinates = set()

        for i2 in range(int(top_left[:-1]), int(bottom_right[:-1]) + 1):
            for i3 in range(ord(top_left[-1]), ord(bottom_right[-1]) + 1):
                temp_ship_coordinates.add(F"{i2}{chr(i3)}")

        intersection = temp_ship_coordinates & hits
        if len(intersection) == len(temp_ship_coordinates):
            sunk = + 1
        elif len(intersection) > 0 and len(intersection) < len(temp_ship_coordinates):
            hit = + 1

    return sunk, hit


sunk, hit = battleship(n, s, t)

print(sunk, hit)
