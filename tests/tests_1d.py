import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

if __name__ == "__main__":
    pytest.main()