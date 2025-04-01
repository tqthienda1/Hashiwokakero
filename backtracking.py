from bridge import *

def Backtracking(clauses):
    variables = set()
    for clause in clauses:
        for literal in clause:
            variables.add(abs(literal))

    variables = sorted(list(variables))

    assignment = [0] * len(variables) 

    def backtrack(index):
        if index == len(variables):
            for clause in clauses:
                clause_satisfied = False
                for literal in clause:
                    var_index = variables.index(abs(literal))
                    value = assignment[var_index]
                    if (literal > 0 and value == 1) or (literal < 0 and value == -1):
                        clause_satisfied = True
                        break
                if not clause_satisfied:
                    return False
            return True

        assignment[index] = 1 
        if backtrack(index + 1):
            return True

        assignment[index] = -1 
        if backtrack(index + 1):
            return True

        assignment[index] = 0
        return False

    if backtrack(0):
        return [variables[i] if assignment[i] == 1 else -variables[i] for i in range(len(variables))]
    else:
        return None