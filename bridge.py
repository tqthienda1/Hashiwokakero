class Bridge:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.num_bridge = None
    
    def __repr__(self):
        return f"Island A: {self.pos1}, Island B: {self.pos2}\n"