from pysat.solvers import Cadical195
from pysat.solvers import Glucose3
from bridge import *
from helper import *

def main():
    solver = Glucose3()
    map_choice = input("Choose input (1-10):")
    game_map = readInput(f"./inputs/input{map_choice}.txt")
    list_of_bridges = initBridges(game_map)
    print("Solving CNF with:")
    print("1. PySAT")
    print("2. A Star")
    print("3. Brute Force")
    print("4. Backtracking")
    choice = input("Enter your choice: ")
    
    start_time = time.time()
    list_of_true_bridges = getAnswer(solver, list_of_bridges, game_map, choice)
    elapsed_time = time.time() - start_time
    
    if list_of_true_bridges:
        printAnswer(list_of_true_bridges, list_of_bridges, game_map)
        print(f"Time(ms): {round(elapsed_time * 1000, 3)}")
    else:
        print("No solution")
    

if __name__ == "__main__":
    main()