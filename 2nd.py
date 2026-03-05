# Program to calculate average, percentage and grade

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

# Calculations
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

# Grade calculation
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

# Output
print("\n----- Result -----")
print(f"Total Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Percentage    : {percentage}%")
print(f"Grade         : {grade}")
