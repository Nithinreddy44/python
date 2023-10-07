import csv
with open('D:\Python\hello.csv','r') as file:
 reader=csv.reader(file,delimiter='\t')
 for row in reader:
       print(row)
