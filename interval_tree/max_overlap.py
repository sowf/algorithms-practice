from typing import List

from .classes import Interval, Node


def max_overlap(intervals: List[Interval]) -> int:
    def insert(root, interval):
        if not root: return Node(interval, interval.hi)

        if interval.lo < root.interval.lo:
            root.left = insert(root.left, interval)
        else:
            root.right = insert(root.right, interval)

        return root

    root = None
    for interval in intervals:
        root = insert(root, interval)

    def count_overlaps(root, interval):
        if not root: return 0

        res = 0
        if root.interval.hi >= interval.lo and interval.hi >= root.interval.lo:
            res += 1
        if root.left and root.left.max >= interval.lo:
            res += count_overlaps(root.left, interval)
        if root.right and root.right.max >= interval.lo:
            res += count_overlaps(root.right, interval)
        return res

    max_overlap = 0
    for interval in intervals:
        max_overlap = max(max_overlap, count_overlaps(root, interval) - 1)

    return max_overlap
