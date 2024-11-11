import csv


movies_path = "C:\\Users\\bullb\\Desktop\\Py\\all_tricks\\movies.csv"

with open(movies_path, newline='', encoding='utf-8') as f:
    file_reader = csv.reader(f, delimiter=",")
    for line in file_reader:
        line = line[0] + ' - ' + line[1]
        print(line)