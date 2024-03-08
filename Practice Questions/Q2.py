#Q2. Write a PYTHON program to calculate the weekly wages of an employee. The pay depends on wages per hour and number of hours worked. Moreover, if the employee has worked for more than 30 hours, then he or she gets twice the wages per hour, for every extra hour that he or she has worked.

wagesperHour,hoursWorked = map(float,input("Enter wages per hour and hours worked by employee: ").split())
if(hoursWorked<=30):
    totalWage = hoursWorked*wagesperHour
else:
    totalWage = 30*wagesperHour + 2*(hoursWorked - 30)*wagesperHour
print("Total Salary : ",totalWage)
