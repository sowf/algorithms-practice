from .classes import Interval
from .overlapping_intervals import overlapping_intervals


def test_1():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    target = Interval(4, 6)
    assert overlapping_intervals(intervals, target) == [Interval(5, 7)]


def test_2():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    target = Interval(0, 2)
    assert overlapping_intervals(intervals, target) == [Interval(1, 3)]


def test_3():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    target = Interval(8, 8)
    assert overlapping_intervals(intervals, target) == []


def test_4():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    target = Interval(9, 12)
    assert overlapping_intervals(intervals, target) == [Interval(9, 11)]


def test_5():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    target = Interval(0, 12)
    assert overlapping_intervals(intervals, target) == intervals
