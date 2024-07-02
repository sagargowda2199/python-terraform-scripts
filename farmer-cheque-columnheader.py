# importing python package
import pandas as pd
import csv

with open('/Users/sagarh/Documents/csv_files_S3/farmer-cheque.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(reader)
print(data)
print(data)

with open("/Users/sagarh/Documents/csv_files_S3_ColumnHeader/farmer-cheque-header.csv", 'w',newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range(len(data)):
        if(i==0):
            wr.writerow(["farmer-cheque-S3"])
        wr.writerow(data[i])