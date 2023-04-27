class Interval:
    def __init__(self, lo: int, hi: int):
        self.lo = lo
        self.hi = hi
    
    def __str__(self):
        return f"[{self.lo}, {self.hi}]"


class Node:
    