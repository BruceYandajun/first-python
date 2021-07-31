numbers = [1, 4, 9, 10, 21]
target = 10


def search(array, t):
    left, right = 0, len(array) - 1
    while left <= right:
        index = left + (right - left) // 2
        if array[index] == t:
            return index
        elif array[index] < t:
            left = index + 1
        else:
            right = index - 1


print(search(numbers, target))

