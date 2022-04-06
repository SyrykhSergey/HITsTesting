import pytest
from main import solution

def test_normal():
    assert solution(5) == 8
def test_normal_second():
    assert solution(142) == 4739
def test_zero():
    assert solution(0) == 0
def test_down_plank():
    assert solution(3) == 3
def test_down_plank_sec():
    assert solution(2) == 0
def test_negative_type():
    assert solution('PudingLor') == 'Иди опохмелись, брат'
def test_negative_number():
    assert solution(-31) == 0

if __name__ == '__main__':
    pytest.main()