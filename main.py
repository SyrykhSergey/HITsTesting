def solution(number):

    if is_int(number):
        number = int(number)
        return sum(x for x in range(number + 1) if x % 3 == 0 or x % 5 == 0)
    else:
        return 0


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def reading_and_writing():
    file_2 = open("ansers.txt", "w")
    file_2.close()
    file_1 = open('arg.txt') #Существует для чтения из файла
    for line in file_1:
        if is_int(line):
            answer = solution(int(line))
        else:
            answer = 0


        file_2 = open('ansers.txt', 'a')
        file_2.write(f'{answer}\n')
    file_2.close()

    file_1.close() #Существует для чтения из файла
    return 0






