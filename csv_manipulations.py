import csv

def open_csv(file_name):
    with open('pacientes/' + file_name + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_array = []
        for row in csv_reader:
            csv_array.append(row)
        return csv_array

def csv_get_attributes(csv_array):
    attributes = 0
    for row in csv_array:
        attributes = row.__len__() - 1
    return attributes

def csv_get_patients(csv_array):
    patients = -1
    for row in csv_array:
        patients += 1
    return patients