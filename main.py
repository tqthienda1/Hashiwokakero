from pysat.solvers import Glucose3
from bridge import *
from helper import *

def main():
    solver = Glucose3()
    game_map = readInput("input.txt")
    list_of_bridges = initBridges(game_map)
    
    bridge_flags = [False] * len(list_of_bridges)
    list_of_true_bridges = getAnswer(solver, list_of_bridges)
    # print(list_of_bridges)
    # print(list_of_true_bridges)
    
    for bridge in range(len(list_of_bridges)):
        if bridge + 1 in list_of_true_bridges:
            print(list_of_bridges[bridge])
    
if __name__ == "__main__":
    main()