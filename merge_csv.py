import csv
data1 = []

with open("final.csv") as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        data1.append(row)

data2 = []

with open("archive_dataset_sorted.csv") as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        data2.append(row)

header1 = data1[0]
header2 = data2[0]

planet_1 = data1[1:]
planet_2 = data2[1:]

data = []
for index, row in enumerate(planet_1):
    data.append(planet_1[index] + planet_2[index])

header = header1 + header2

with open("merged_dataset.csv", "w", newline = "") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(data)