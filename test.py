def generate_at_least_N_CNF(self):
        constrains = []
        if self.numOfBridge == len(self.list_of_brigdes):
            constrains.extend([list(combo) for combo in combinations(self.list_of_brigdes, 1)])
            return constrains
        
        for i in range(1, self.numOfBridge + 1):
            j = i - 1
            if j == 0:
                constrains.extend([list(self.list_of_brigdes)])
                continue
            elif j == 1:
                for k in range(len(self.list_of_brigdes)):
                    clause = [self.list_of_brigdes[j] if j != k else -self.list_of_brigdes[j] for j in range(len(self.list_of_brigdes))]
                    constrains.extend([clause])
                continue
            else:
                temp_list = []
                for combo in combinations(self.list_of_brigdes, j):
                    temp_list.append([-var for var in combo])

                for k in range(len(temp_list)):
                    list_of_brigde_copy = list(self.list_of_brigdes)
                    for l in range(len(list_of_brigde_copy)):
                        for negate_bridge in temp_list[k]:
                            if -list_of_brigde_copy[l] == negate_bridge:
                                list_of_brigde_copy[l] = -list_of_brigde_copy[l]
                    constrains.extend([list_of_brigde_copy])
        return constrains

def generate_at_most_N_CNF(self):
    constrains = []
    if self.numOfBridge == len(self.list_of_brigdes):
        return constrains
    for i in range (self.numOfBridge + 1, len(self.list_of_brigdes) + 1):
        temp_list = []
        for combo in combinations(self.list_of_brigdes, i):
            temp_list.append([-var for var in combo])
        for j in range(len(temp_list)):
                list_of_brigde_copy = list(self.list_of_brigdes)
                for k in range(len(list_of_brigde_copy)):
                    for negate_bridge in temp_list[j]:
                        if -list_of_brigde_copy[k] == negate_bridge:
                            list_of_brigde_copy[k] = -list_of_brigde_copy[k]
                constrains.extend([list_of_brigde_copy])
    return constrains