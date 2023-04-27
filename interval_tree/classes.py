from typing import List


class Interval:
    def __init__(self, lo: int, hi: int):
        self.lo = lo
        self.hi = hi
    
    def __str__(self):
        return f"[{self.lo}, {self.hi}]"


class Node:
    def __init__(self, interval: Interval, max_val: int):
        self.max_val = max_val
        self.interval = interval
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node(interval={self.interval}, max_val={self.max_val})"


class IntervalTree:
    def __init__(self, intervals: List[Interval]):
        self.root = None
        self.build_tree(intervals)

    @staticmethod
    def _insert(root, interval):
        if not root: return Node(interval, interval.hi)

    def insert(self, interval: Interval):
        self.root = self._insert(self.root, interval)

    def build_tree(self, intervals: List[Interval]):
        for interval in intervals:
            self.insert(interval)
