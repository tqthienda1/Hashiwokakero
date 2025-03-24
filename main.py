from pysat.solvers import Glucose3
from bridge import *
from helper import *

def main():
    game_map = readInput("input.txt")
    list_of_bridges = initBridges(game_map)
    print(list_of_bridges) 

if __name__ == "__main__":
    main()