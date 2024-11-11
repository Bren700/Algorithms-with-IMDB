import csv


movie_arr = []

with open('movies.csv', newline='', encoding='utf-8') as f:
    file_reader = csv.reader(f, delimiter=",")
    for line in file_reader:
        movie_arr.append(line)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubblesort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1][1] > arr[i][1]:
                swap(arr, i - 1, i)
                swapped = True


rated_arr = []
def found_binary(array, value):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low+high) // 2
        if array[middle][1] == value:
            break
        elif array[middle][1] > value:
            high = middle - 1
        else:
            low = middle + 1
    else:
        return -1

    i = middle
    while i >= 0 and array[i][1] == value:
        rated_arr.append(array[i])
        i -= 1

    i = middle + 1
    while i < len(array) and array[i][1] == value:
        rated_arr.append(array[i])
        i += 1

if __name__ == '__main__':
    bubblesort(movie_arr)
    found_binary(movie_arr, '6.0')
    for line in rated_arr:
        line = line[0] + ' - ' + line[1]
        print(line)
