import csv


with open('eggs.csv', 'w', newline='') as file:
    spam_writer = csv.writer(file)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful spam'])


with open('eggs.csv', 'r', newline='') as file:
    spam_reader = csv.reader(file)
    for row in spam_reader:
        print(', '.join(row))



with open('names.csv', 'w', newline='') as file:
    fields_names = ['first_name', 'last_name']
    writer = csv.DictWriter(file, fieldnames=fields_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus'})
    writer.writerow({'first_name': 'David', 'last_name': 'Kryndushkin'})
    writer.writerow({'first_name': 'Oksana', 'last_name': 'Apushkina'})
    writer.writerow({'first_name': 'Misha'})


with open('names.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['first_name'], row['last_name'])