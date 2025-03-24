from bridge import *

def readInput(file_name):
    game_map = []
    with open(file_name, 'r') as f:
        for line in f:
            game_map.append(list(map(int, line.split(", "))))
    
    return game_map

def initBridges(game_map):
    list_of_bridges = []
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] > 0:
                for right in range(x + 1, len(game_map[0])):
                    if game_map[y][right] > 0:
                        list_of_bridges.append(Bridge((y, x), (y, right), 1))
                        list_of_bridges.append(Bridge((y, x), (y, right), 1))
                        break
                for down in range(y + 1, len(game_map)):
                    if game_map[down][x] > 0:
                        list_of_bridges.append(Bridge((y, x), (down, x), 1))
                        list_of_bridges.append(Bridge((y, x), (y, right), 2))
                        break
                    
    return list_of_bridges

