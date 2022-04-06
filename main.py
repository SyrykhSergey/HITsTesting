def solution(number):
    if (type(number) == int):
        return sum(x for x in range(number+1) if x % 3 == 0 or x % 5 == 0)
    else:
        return("Иди опохмелись, брат")