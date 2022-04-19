import pytest
import uidesign
from main import reading_and_writing
from main import solution
from PyQt5 import QtCore



def test_normal():
    file_1 = open("ansers.txt")
    file_2 = open("arg.txt")
    reading_and_writing()
    answ_1 = []
    answ_2 = []
    for line in file_1:
        answ_2.append(int(line))
    for line in file_2:
        answ_1.append(solution(line))

    assert answ_2 == answ_1