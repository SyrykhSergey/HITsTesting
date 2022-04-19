import pytest

import uidesign
import pytest
import pytestqt
from main import reading_and_writing
from main import solution
from PyQt5 import QtCore

@pytest.fixture
def widget(qtbot):#Частично украл у индуса :)
    widget = uidesign.Ui_MainWindow()
    qtbot.addWidget(widget)

    return widget

def test_clicking_button(app, qtbot):

    qtbot.MouseClick(widget.pushButton, QtCore.Qt.leftButton)
    assert widget.label_2.text() == "ОК, проверьте ansers"
def test_solution_with_ui(app, qtbot):
    qtbot.MouseClick(widget.pushButton, QtCore.Qt.leftButton)
    file_1 = open("ansers.txt")
    file_2 = open("arg.txt")
    answ_1 = []
    answ_2 = []
    for line in file_1:
        answ_2.append(int(line))
    for line in file_2:
        answ_1.append(solution(line))

    assert answ_2 == answ_1


if __name__ == '__main__':
    pytest.main()
