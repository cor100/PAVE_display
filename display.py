import csv 
with open('/var/www/html/test_csv.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
while (True):
    #Write data to file in CSV format
    with open ('/var/www/html/data.csv','a') as datafile:
        datafile.write(str(temperatureSensor.getTemperature()) + "\n")  