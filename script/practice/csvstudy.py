import csv
csv_file=csv.reader(open("stu_info.csv","r"))
for stu in csv_file:
    print(stu)
    # print(stu[0])
    # print(stu[1])
    # print(stu[2])
