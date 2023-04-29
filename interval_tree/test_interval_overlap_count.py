from .classes import Interval

from .interval_overlap_count import interval_overlap_count


def test_1():
    intervals = [Interval(1, 3), Interval(2, 4), Interval(4, 5)]
    assert interval_overlap_count(intervals) == [1, 2, 1]


def test_2():
    intervals = [Interval(1, 4), Interval(2, 6), Interval(5, 7)]
    assert interval_overlap_count(intervals) == [1, 2, 1]


def test_3():
    intervals = [Interval(1, 3), Interval(4, 6), Interval(7, 9)]
    assert interval_overlap_count(intervals) == [0, 0, 0]


def test_4():
    intervals = [Interval(1, 3), Interval(2, 5), Interval(4, 6)]
    assert interval_overlap_count(intervals) == [1, 2, 1]


def test_5():
    intervals = [Interval(1, 3), Interval(3, 7), Interval(9, 11)]
    assert interval_overlap_count(intervals) == [1, 1, 0]
