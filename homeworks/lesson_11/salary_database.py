import csv

salaries = []
with open('salaries.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1].isnumeric():
            salaries.append(int(row[1]))

maximal = max(salaries)
minimal = min(salaries)
average = sum(salaries)/len(salaries)


# create new file
header = ['TYPE', 'SALARY']
rows = [['Minimum salary', minimal], ['Maximum salary', maximal], ['Average salary', average]]
with open('stats.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)