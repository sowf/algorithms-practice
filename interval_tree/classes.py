from typing import List


class Interval:
    def __init__(self, lo: int, hi: int):
        self.lo = lo
        self.hi = hi

    def __eq__(self, other):
        return self.lo == other.lo and self.hi == other.hi
    
    def __str__(self):
        return f"[{self.lo}, {self.hi}]"

    def __repr__(self):
        return str(self)


class Node:
    def __init__(self, interval: Interval, max_val: int):
        self.max = max_val
        self.interval = interval
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node(interval={self.interval}, max_val={self.max}, left={self.left}, right={self.right})"


class IntervalTree:
    def __init__(self, intervals: List[Interval]):
        self.root = None
        self.build_tree(intervals)

    def _insert(self, root, interval):
        if not root: return Node(interval, interval.hi)

        if interval.lo < root.interval.lo:
            root.left = self._insert(root.left, interval)
        else:
            root.right = self._insert(root.right, interval)

        if interval.hi > root.max:
            root.max = interval.hi

        return root

    def insert(self, interval: Interval):
        self.root = self._insert(self.root, interval)

    def build_tree(self, intervals: List[Interval]):
        for interval in intervals:
            self.insert(interval)
