s1,s2,s3,s4,s5 = map(int, input("Enter marks of a student in 5 subjects(out of 100): ").split())
totalMarks=s1+s2+s3+s4+s5;
percentage = totalMarks/500 *100
print("Total Marks= ",totalMarks)
print("Percentage= ",percentage)
if percentage<=45:
    print("Fail")
elif percentage>45 and percentage<=60:
    print("Pass")
elif percentage>60 and percentage<=75:
    print("Good")
elif percentage>75 and percentage<=85:
    print("Very Good")
elif percentage>85 and percentage<=100:
    print("Excellent")
else:
    print("Error")