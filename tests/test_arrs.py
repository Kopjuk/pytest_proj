from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.my_slice([1, 2, 3], 0) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.get([], -1) is None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([], ) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4], -3, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, -2) == [2]
    assert arrs.my_slice([1, 2, 3, 4], -1, -3) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3, 4], 1, 9) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3], 4, 6) == []
