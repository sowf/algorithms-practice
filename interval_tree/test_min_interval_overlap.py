from .classes import Interval

from .min_interval_overlap import min_interval_overlap


def test_1():
    intervals = [Interval(1, 3), Interval(5, 7), Interval(9, 11)]
    assert min_interval_overlap(intervals) == 0.0


def test_2():
    intervals = [Interval(1, 3), Interval(2, 4), Interval(3, 5)]
    assert min_interval_overlap(intervals) == 1.0


def test_3():
    intervals = [Interval(1, 5), Interval(2, 6), Interval(3, 7)]
    assert min_interval_overlap(intervals) == 0.0


def test_4():
    intervals = [Interval(1, 3), Interval(4, 6), Interval(7, 9)]
    assert min_interval_overlap(intervals) == float('inf')


def test_5():
    intervals = [Interval(1, 3), Interval(2, 5), Interval(4, 6)]
    assert min_interval_overlap(intervals) == 0.0
