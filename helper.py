from bridge import *
from pysat.solvers import Glucose3
from pysat.card import CardEnc

def readInput(file_name):
    game_map = []
    with open(file_name, 'r') as f:
        for line in f:
            game_map.append(list(map(int, line.split(", "))))
    
    return game_map
# x1  > x2 and y3 > y4
def isCrossing(bridgeA, bridgeB):
    (y1A, x1A), (y2A, x2A) = bridgeA.pos1, bridgeA.pos2
    (y1B, x1B), (y2B, x2B) = bridgeB.pos1, bridgeB.pos2

    if y1A == y2A and x1B == x2B:  
        return (x1A < x1B < x2A) and (y1B < y1A < y2B)
    if x1A == x2A and y1B == y2B: 
        return (y1A < y1B < y2A) and (x1B < x1A < x2B)

    return False

def crossingConstraint(solver, list_of_bridges):
    for bridgeA in range(len(list_of_bridges)):
        for bridgeB in range(bridgeA + 1, len(list_of_bridges)):
            if isCrossing(list_of_bridges[bridgeA], list_of_bridges[bridgeB]):
                solver.add_clause([-(bridgeA + 1), -(bridgeB + 1)])
                solver.add_clause([(bridgeA + 1), (bridgeB + 1)])
                

def oneBridgeTypeConstraint(solver, list_of_bridges):
    for bridge in range(0, len(list_of_bridges), 2):
        solver.add_clause([-(bridge + 1), -(bridge + 2)])
        solver.add_clause([(bridge + 1), (bridge + 2)])
        
        
def initBridges(game_map):
    list_of_bridges = []
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] > 0:
                for right in range(x + 1, len(game_map[0])):
                    if game_map[y][right] > 0:
                        list_of_bridges.append(Bridge((y, x), (y, right), 1))
                        list_of_bridges.append(Bridge((y, x), (y, right), 2))
                        break
                for down in range(y + 1, len(game_map)):
                    if game_map[down][x] > 0:
                        list_of_bridges.append(Bridge((y, x), (down, x), 1))
                        list_of_bridges.append(Bridge((y, x), (down, x), 2))
                        break
                    
    return list_of_bridges

def getAnswer(solver, list_of_bridges):
    crossingConstraint(solver, list_of_bridges)
    oneBridgeTypeConstraint(solver, list_of_bridges)
    
    if solver.solve():
        pySatAnswer = solver.get_model()
        print(pySatAnswer)
        list_of_true_bridges = list(filter(lambda i: i > 0, pySatAnswer))
        return list_of_true_bridges
        
    
    return None