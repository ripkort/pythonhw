#!/usr/bin/env python3

import random

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
field_s = 10

def field_generator():
    return [[['*', '0'] for x in range(field_s)] for y in range(field_s)]

def rand_num():
    x = random.randint(0, field_s - 1)
    y = random.randint(0, field_s - 1)
    return x, y

def ship_generator(x, y, _direction, _ship_length):
    _around_cells = set()
    ship_cells = set()

    for cell in range(_ship_length):
        if (x + _ship_length > 10 and _direction == 0) or (y + _ship_length > 10 and _direction == 1):
            cell *= -1

        _x = x + cell * int(not _direction)
        _y = y + cell * _direction
        
        #save position of ship
        ship_cells.add((_x, _y))

        #save cells around the ship
        for n in range(_x - 1, _x + 1):
            for m in range(_y - 1, _y + 1):
                _around_cells.add((n, m))

    return _around_cells, ship_cells

def ships_generator(_ships):

    used_cells = set()
    field = field_generator()

    for ship_length in ships:

        x, y = rand_num()
 
        #0 - increment x, 1 - increment y
        direction = random.randint(0,1)

        around_cells, ship_cells = ship_generator(x, y, direction, ship_length)

        #check if cells with ship and around were already used
        while around_cells.intersection(used_cells):
            x, y = rand_num()
            around_cells, ship_cells = ship_generator(x, y, direction, ship_length) 
        
        #saving all already used cells
        used_cells.update(around_cells)

        #put ship on the field
        for cell in ship_cells:
            field[cell[0]][cell[1]][1] = '1'

    return field

def print_field(field, _field_s):

    print("Type x and y with space or 'q' for exit")

    #vertical numeration
    i = 0

    #horizontal numeration
    print('  ' + ' '.join([str(x) for x in range(_field_s)]))

    for row in field:

        #vertical numeration
        print(i, end=' ')
        i +=1

        for cell in row:
            print(' '.join(cell[0]),end=' ')
        print()


def game(field_s):

    score = 0

    printed_field = ships_generator(ships)
    print_field(printed_field, field_s) 
   
    while score != 20:

        answer = input()
        if answer == 'q':
            break

        else:

            try:
                y, x = [int(a) for a in answer.split()]
            except:
                print("Please input two digits with space between")
                continue

        if x > 9 or y > 9:
            print("Please input number between 0 and {}".format(field_s - 1))

        #check if cell has ship
        elif printed_field[x][y][1] == '1':
            #mark representation cell
            printed_field[x][y][0] = 'X'
            score += 1
            print_field(printed_field, field_s)
        else:
            print("You missed! Try again. You need to get 20 scores. You have {}".format(score))

if __name__ == "__main__":
    game(field_s)
