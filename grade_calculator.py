print("=================================")
print("     Student Grade Calculator    ")
print("=================================")

name = input("Enter student name: ")

math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))
computer = int(input("Enter Computer marks: "))
kannada = int(input("Enter Kannada marks: "))

total = math + english + science + computer + kannada
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
