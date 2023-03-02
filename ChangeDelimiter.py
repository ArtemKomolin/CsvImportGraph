import csv

with open("data_test.csv", "r", encoding="utf_8_sig") as f:
    reader = csv.reader(f, delimiter=";")

    data = []
    for row in reader:
        data.append({'id_события': row[0], 'ФИО_участника_события_1': row[1], 'ФИО_участника_события_2': row[2]})

del data[0]

with open("data.csv", "w", encoding="utf_8_sig") as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),  delimiter=',')
    writer.writeheader()
    for d in data:
        writer.writerow(d)


