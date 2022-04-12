def solution(number):
    if (type(number) == int):
        return sum(x for x in range(number + 1) if x % 3 == 0 or x % 5 == 0)
    else:
        return ("Иди опохмелись, брат")


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def reading_and_writing(number):
    #file_1 = open('arg.txt') Существует для чтения из файла
    #for line in file_1:
    if is_int(number):
        answer = solution(int(number))
    else:
        answer = "net net net"


    file_2 = open('answers.txt', 'a')
    file_2.write(f'{answer} for number - {number} \n')
    file_2.close()

    #file_1.close() Существует для чтения из файла
    return 0


reading()
