import csv

def readFile(nameoffile):
    with open(nameoffile, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)