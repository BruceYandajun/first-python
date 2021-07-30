numbers = [1, 4, 9, 10, 21]
target = 9

def search (l, t):
    index = 0
    for i in l:
        if i == t:
            return index
        index += 1

