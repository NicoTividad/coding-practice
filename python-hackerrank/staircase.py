n = 3

def staircase(n):
    count = n 
    for hash in range(1, count):
        gap = count - hash
        print(" " * gap, end= '')
        print("#" * hash)

staircase(n)