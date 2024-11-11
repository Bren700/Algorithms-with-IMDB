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


bubblesort(movie_arr)
for line in movie_arr:
    line = line[0] + ' - ' + line[1]
    print(line)