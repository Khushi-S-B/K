ERROR
import csv
with open('C:/khushipyythonn/employeedata.csv,'w') as csvFile:
          ptr=csv.writer(csvFile)
          ptr.writerow(['eno','name','sal','gender'])
          ptr.writerow([1,'a',5000,'M'])
          
