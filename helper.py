from bridge import *
from pysat.solvers import Glucose3
from pysat.card import CardEnc
from itertools import combinations  
from a_star import *
from brute_force import *
from collections import defaultdict
from backtracking import *
import time


def readInput(file_name):
    game_map = []
    with open(file_name, 'r') as f:
        for line in f:
            game_map.append(list(map(int, line.split(", "))))
    
    return game_map

def isCrossing(bridgeA, bridgeB):
    if bridgeA.pos1 == bridgeB.pos1 and bridgeA.pos2 == bridgeB.pos2:
        return False
    (y1A, x1A), (y2A, x2A) = bridgeA.pos1, bridgeA.pos2
    (y1B, x1B), (y2B, x2B) = bridgeB.pos1, bridgeB.pos2

    if y1A == y2A and x1B == x2B:  
        return (x1A < x1B < x2A) and (y1B < y1A < y2B)
    if x1A == x2A and y1B == y2B: 
        return (y1A < y1B < y2A) and (x1B < x1A < x2B)

    return False

def crossingConstraint(solver, list_of_bridges, a_star_solver):
    for bridgeA in range(len(list_of_bridges)):
        for bridgeB in range(bridgeA + 1, len(list_of_bridges)):
            if isCrossing(list_of_bridges[bridgeA], list_of_bridges[bridgeB]):
                a_star_solver.append([-(bridgeA + 1), -(bridgeB + 1)])
                
                solver.add_clause([-(bridgeA + 1), -(bridgeB + 1)])
                
                
def numBridgeConnectToIslandConstraint(solver, game_map, list_of_bridges, a_star_solver):
    for y in range(len(game_map)):
        for x in range(len(game_map)):
            if game_map[y][x] > 0:
                neighbor_bridges = [i + 1 for i, bridge in enumerate(list_of_bridges) if bridge.pos1 == (y, x) or bridge.pos2 == (y, x)]
                
                
                if neighbor_bridges:
                    for subset in combinations(neighbor_bridges, len(neighbor_bridges) - game_map[y][x] + 1):
                        a_star_solver.append(list(subset))
                        solver.add_clause(list(subset))
                    
                    for subset in combinations(neighbor_bridges, game_map[y][x] + 1):
                        a_star_solver.append([-x for x in subset])
                        solver.add_clause([-x for x in subset])

def initBridges(game_map):
    list_of_bridges = []
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] > 0:
                for right in range(x + 1, len(game_map[0])):
                    if game_map[y][right] > 0:
                        list_of_bridges.append(Bridge((y, x), (y, right)))
                        list_of_bridges.append(Bridge((y, x), (y, right)))
                        break
                for down in range(y + 1, len(game_map)):
                    if game_map[down][x] > 0:
                        list_of_bridges.append(Bridge((y, x), (down, x)))
                        list_of_bridges.append(Bridge((y, x), (down, x)))
                        break
                    
    return list_of_bridges

def getAnswer(solver, list_of_bridges, game_map, choice):
    a_star_solver = []
    crossingConstraint(solver, list_of_bridges, a_star_solver)
    numBridgeConnectToIslandConstraint(solver, game_map, list_of_bridges, a_star_solver)
    
    list_of_true_bridges = []
    if choice == "1": 
        if solver.solve():
            pySatAnswer = solver.get_model()
            list_of_true_bridges = list(filter(lambda i: i > 0, pySatAnswer))
        print("PySAT")
    elif choice == "2":
        AStarAnswer = AStar(a_star_solver, list_of_bridges)
        
        if AStarAnswer is not None:
            list_of_true_bridges = list(filter(lambda i: i > 0, AStarAnswer))
        else:
            list_of_bridges = []
        print("A*")
    elif choice == "3":
        BruteForceAnswer = brute_force(a_star_solver, list_of_bridges)
        
        if BruteForceAnswer is not None:
            list_of_true_bridges = list(filter(lambda i: i > 0, BruteForceAnswer))
        else:
            list_of_true_bridges = []
        print("BF")
    elif choice == "4":
        BacktrackingAnswer = Backtracking(a_star_solver)
        
        if BacktrackingAnswer is not None:
            list_of_true_bridges = list(filter(lambda i: i > 0, BacktrackingAnswer))
        else:
            list_of_true_bridges = []
        print("Backtracking")

    return list_of_true_bridges   
        

def printAnswer(list_of_true_bridges, list_of_bridges, game_map):
    for num_bridge in list_of_true_bridges:
        bridge = list_of_bridges[num_bridge - 1]
        
        if bridge.pos1[0] == bridge.pos2[0]:
            for pos in range(bridge.pos1[1] + 1, bridge.pos2[1]):
                if game_map[bridge.pos1[0]][pos] == 0:
                    game_map[bridge.pos1[0]][pos] = '-'
                elif game_map[bridge.pos1[0]][pos] == '-':
                    game_map[bridge.pos1[0]][pos] = '='
        elif bridge.pos1[1] == bridge.pos2[1]:
            for pos in range(bridge.pos1[0] + 1, bridge.pos2[0]):
                if pos == 1 and bridge.pos1[1] == 1:
                    print(num_bridge)
                if game_map[pos][bridge.pos1[1]] == 0:
                    game_map[pos][bridge.pos1[1]] = '|'
                elif game_map[pos][bridge.pos1[1]] == '|':
                    game_map[pos][bridge.pos1[1]] = '$'
                    
    game_map = [[str(item) for item in row] for row in game_map]
    for line in game_map:
        print(line)