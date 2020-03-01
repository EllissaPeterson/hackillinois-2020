import os
import csv
import git
import array as arr

import Messages_pb2;

def get_data(date):
    git.Git(".").clone("git://github.com/CSSEGISandData/COVID-19.git")
    
    for filename in os.listdir('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'):
        if filename.endswith('.csv') != true:
            continue
        
        file_date = Messages_pb2.Date()
        file_date.month = int(filename[:2])
        file_date.day = int(filename[3:5])
        file_date.year = int(filename[6:10])
        row.date = file_date
        
        if file_date.year < date.year:
            return -1
        elif file_date.year == date.year:
            if file_date.month < date.month:
                return -1
            elif file_date.month == date.month:
                if file_date.day < date.day:
                    return -1
        
        file = open(filename, 'r')
        reader = csv.reader(file, delimiter=',')
        
        data = Messages_pb2.Dump()
        
        for row in reader:
            row = Messages_pb2.Row()
            
            row.location = get_location(row[2], row[1])
            row.confirmed_cases = row[4]
            row.confirmed_deaths = row[5]
            row.confirmed_recovered = row[6]
            row.date = file_date;
            
            data.append(row)
        
        return data


def get_location(country, province):
    file = open('latlong.csv', 'r')
    reader = csv.reader(file, delimiter=',')
    
    i = 0
    for row in reader:
        if row[1].lower() == country.lower() and row[2].lower() and province.lower():
            location = Messages_pb2.Location()
            location.latitude = row[3]
            location.longitude = row[4]
            return location 
        i += 1
    
    return -1