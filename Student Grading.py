# Program to accept student's marks and print grade

# Take input from user
marks = int(input("Enter student's marks: "))

# Check conditions for grade
if marks >= 85:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")