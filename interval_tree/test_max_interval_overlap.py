from .classes import Interval

from .max_interval_overlap import max_interval_overlap


def test_1():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    assert max_interval_overlap(intervals) == 0


def test_2():
    intervals = [Interval(1, 3), Interval(2, 4), Interval(2, 5)]
    assert max_interval_overlap(intervals) == 2


def test_3():
    intervals = [Interval(1, 5), Interval(2, 6), Interval(5, 7)]
    assert max_interval_overlap(intervals) == 3


def test_4():
    intervals = [Interval(1, 3), Interval(4, 6), Interval(6, 9)]
    assert max_interval_overlap(intervals) == 0


def test_5():
    intervals = [Interval(1, 3), Interval(2, 5), Interval(4, 6)]
    assert max_interval_overlap(intervals) == 1
