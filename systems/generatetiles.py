import random

def tile_generation():

    # River generation
    river_location_x = random.randint(0, 4)

    if random.randint(1, 100) <= 50:
        river_location_y = 0
        river_start = 'bottom'
    else:
        river_location_y = 4
        river_start = 'top'

    river_list = []

    while river_location_y != -1 and river_location_y != 5 and river_location_x != -1 and river_location_x != 5:
        river_list.append([river_location_x, river_location_y])

        # Even
        if river_location_y % 2 == 0:
            river_location_x -= random.randint(0, 1)

        # Odd
        else:
            river_location_x += random.randint(0, 1)

        if river_start == 'top':
            river_location_y -= 1

        elif river_start == 'bottom':
            river_location_y += 1

    # Remaining tile generation
    tiles = ['grassland', 'hills', 'forest', 'marsh', 'swamp', 'mountain', 'lake']

    tile_list = random.choices(tiles, weights=(20, 20, 20, 20, 10, 10, 5), k=(25-len(river_list)))

    return river_list, tile_list