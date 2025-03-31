from itertools import product
from bridge import *

def evaluate_clause(clause, assignment):
    return any((lit > 0 and assignment[abs(lit)]) or (lit < 0 and not assignment[abs(lit)]) for lit in clause)

def brute_force(cnf, list_of_bridges):
    for bits in product([False, True], repeat=len(list_of_bridges)):  
        assignment = {i + 1: bits[i] for i in range(len(list_of_bridges))}  
        if all(evaluate_clause(clause, assignment) for clause in cnf):  
            res = []
            for c in assignment:
                if assignment[c]:
                    res.append(c)
            return res
    return None  