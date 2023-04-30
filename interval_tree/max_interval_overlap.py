from typing import List

from .classes import Interval, Node


def max_interval_overlap(intervals: List[Interval]) -> float:
    def insert(root, interval):
        if not root: return Node(interval, interval.hi)

        if interval.lo < root.interval.lo:
            root.left = insert(root.left, interval)
        else:
            root.right = insert(root.right, interval)

        if interval.hi > root.max:
            root.max = interval.hi

        return root

    root = None
    for interval in intervals:
        root = insert(root, interval)

    def get_max_overlap(root, interval):
        if not root: return 0

        if root.interval == interval:
            return 0

        res = 0
        if interval.lo <= root.interval.hi and interval.hi >= root.interval.lo:
            res = max(
                res,
                root.interval.hi - interval.lo,
            )
        if root.left and interval.lo <= root.left.max:
            res = max(res, get_max_overlap(root.left, interval))
        if root.right and interval.lo <= root.right.max:
            res = max(res, get_max_overlap(root.right, interval))
        return res

    max_overlap = 0
    for interval in intervals:
        max_overlap = max(max_overlap, get_max_overlap(root, interval))

    return max_overlap
