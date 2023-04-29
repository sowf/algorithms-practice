from typing import List

from .classes import Interval, Node


def overlapping_intervals(intervals: List[Interval], target: Interval) -> List[Interval]:
    def insert(root: Node, interval: Interval):
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


    def find_overlapping(root: Node, interval: Interval):
        if not root: return []

        result = []
        if interval.lo <= root.interval.hi and interval.hi >= root.interval.lo:
            result += [root.interval]
        if root.left and interval.lo <= root.left.max:
            result += find_overlapping(root.left, interval)
        if root.right and interval.lo <= root.right.max:
            result += find_overlapping(root.right, interval)

        return result

    return find_overlapping(root, target)
