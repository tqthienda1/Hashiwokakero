from bridge import *
import heapq
from itertools import combinations

def goalState(state, a_star_solver):
    for clause in a_star_solver:
        if not any(lit in state for lit in clause):
            return False
        
    return True

def heuristic(state, new_state, a_star_solver):
    value = 0
    
    for clause in a_star_solver:
        if not any(lit in new_state for lit in clause):
            value += 1
            
    return value 

def AStar(a_star_solver, list_of_bridges):
    frontier = []
    heapq.heappush(frontier, (0, [], 1))
    
    while frontier:
        f, state, cur_var = heapq.heappop(frontier)
        # print(state)
        if len(state) == len(list_of_bridges):
            if goalState(state, a_star_solver):
                return state
            continue
        
        
        for value in [-cur_var, cur_var]:
            new_state = state + [value]
            g = len(state)
            h = heuristic(state, new_state, a_star_solver)
            heapq.heappush(frontier, ((g + h), new_state, cur_var + 1))
            
    return None
        