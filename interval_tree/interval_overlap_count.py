from typing import List

from .classes import Interval, Node


def interval_overlap_count(intervals: List[Interval]) -> List[int]:
    def insert(root, interval):
        if not root: return Node(interval, interval.hi)

        if interval.lo < root.interval.lo:
            root.left = insert(root.left, interval)
        else:
            root.right = insert(root.right, interval)

        if root.max < interval.hi:
            root.max = interval.hi

        return root

    root = None
    for interval in intervals:
        root = insert(root, interval)

    def count(root, interval):
        if not root: return 0

        res = 0
        if interval.lo <= root.interval.hi and interval.hi >= root.interval.lo:
            res += 1
        if root.left and interval.lo <= root.left.max:
            res += count(root.left, interval)
        if root.right and interval.lo <= root.right.max:
            res += count(root.right, interval)

        return res


    return [count(root, interval) - 1 for interval in intervals]
