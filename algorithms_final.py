import csv


movie_arr = []
rated_arr = []

with open('movies.csv', newline='', encoding='utf-8') as f:
    file_reader = csv.reader(f, delimiter=",")
    for line in file_reader:
        movie_arr.append(line)


def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)


def merge(arr, left, middle, right):
    len1 = (middle - left) + 1
    len2 = right - middle

    left_arr = [0] * len1
    right_arr = [0] * len2

    for i in range(len1):
        left_arr[i] = arr[left + i]

    for j in range(len2):
        right_arr[j] = arr[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < len1 and j < len2:
        if left_arr[i][1] <= right_arr[j][1]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


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
    merge_sort(movie_arr, 0, len(movie_arr)-1)
    found_binary(movie_arr, '6.0')
    for line in rated_arr:
        line = line[0] + ' - ' + line[1]
        print(line)