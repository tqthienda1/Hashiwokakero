from pysat.solvers import Glucose3
from bridge import *
from helper import *

def main():
    solver = Glucose3()
    game_map = readInput("input.txt")
    list_of_bridges = initBridges(game_map)
    print("Solving CNF with:")
    print("1. PySAT")
    print("2. A Star")
    print("3. Brute Force")
    print("4. Backtracking")
    choice = input("Enter your choice: ")
    
    list_of_true_bridges = getAnswer(solver, list_of_bridges, game_map, choice)
    # if list_of_true_bridges:
    #     for bridge in range(len(list_of_bridges)):
    #         if bridge + 1 in list_of_true_bridges:
    #             print(f"#{bridge}" ,list_of_bridges[bridge])
                
    printAnswer(list_of_true_bridges, list_of_bridges, game_map)
    
    
if __name__ == "__main__":
    main()