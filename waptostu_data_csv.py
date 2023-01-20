import csv

def recordcsv():
    f = open('stu.csv','a')
    fw = csv.writer(f)
    format = ['Roll no.','Name','Number']
    fw.writerow(format)
    for i in range(1,4):
        rno = int(input("Enter Roll no: "))
        name = input('Enter Name: ')
        num = int(input('Enter Number: '))
        dat = [rno,name,num]
        fw.writerow(dat)
    f.close()

recordcsv()