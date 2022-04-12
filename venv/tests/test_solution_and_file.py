import pytest
from main import reading_and_writing


def test_normal():
    numbers = [3, 5, 15, 0, -15, 'alkanoid', 13.1]
    answers = [3, 8, 60, 0, 0, 0, 45]
    answers_from_file = []
    for number in numbers:
        reading_and_writing(number)
    file = open("ansers.txt")
    for line in file:
        answers_from_file.append(int(line))

    assert answers_from_file == answers

    file.close()#К слову нахрен эта дурь нужна
    file = open("ansers.txt", "w")#Т.к. код записи сделан дерьмово и не особо то и рассчитан на тесты
    file.close()#Мы можем убрать эти строки и всё будет работать... Один раз, потом нужно будет очистить ответы
                #и так снова и снова, а кому это надо, мне вот лень, поэтому здесь и эти 3 вонючие строки





if __name__ == '__main__':
    pytest.main()
