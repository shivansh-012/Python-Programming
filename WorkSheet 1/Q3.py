grade = input("Enter Student's Grade: ")[0]
if grade.upper() == 'A':
    print("Outstanding")
elif grade.upper() == 'B':
    print("Excellent")
elif grade.upper() == 'C':
    print("Very Good")
elif grade.upper() == 'D':
    print("Satisfactory")
else:
    print("Unreognized")