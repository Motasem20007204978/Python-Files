import csv
'''
txt = Sabrina Green, 802-867-5309, System Administrator
Eli Jones, 684-3481127, IT specialist
Melody Daniels, 846 -687-7436, Progranmer
Charlie Rivera, 698-746-3357, Web Developer

f = open('file.txt', 'w')
f.write(txt); f.flush(); f.close()
'''
f = open('file.txt')

csv_f = csv.reader(f)
writer = csv.writer(open('file.csv', 'a'))

for row in csv_f:
    name, phone, role = row
    print(f'Name: {name}, Phone: {phone}, and Role: {role}')
    writer.writerow(row)

Users = [{'name': 'Sol Mans', 'username': 'solm', 'department': 'IT infrastructure'},
        {'name': 'Lio Nelson', 'username': 'lion', 'department':'UX research'},
        {'name': 'Charlie Grey', 'username': 'grayc', 'department': 'development'}]

keys = Users[0].keys()

with open('file2.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(Users)

with open('file2.csv') as f2:
    reader = csv.DictReader(f2)
    print(reader.line_num)
    for row in reader:
        print(('{} has {}').format(row['name'], row['username']))