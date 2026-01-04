result = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student's name: \n")
    marks = []
    subject = input("Enter subject's name with space: \n").split()
    for j in subject:
        mark = int(input(f"Enter marks of {j}: \n"))
        marks.append(mark)

    result[name] = marks
    
topper = ""
highest_percentage = 0

for name , marks in result.items():
    total = sum(marks)
    percentage = total/len(marks)

    if(percentage >= 33):
        status = "PASS"
    else:
        status = "FAIL"
    print(f"{name}: Total marks: {total}\nPercentage: {percentage:.2f}%\nResult: {status} ")

    if (percentage > highest_percentage):
        highest_percentage = percentage
        topper = name

print(f"Topper: {topper}\n Percentage: {highest_percentage:.2f}%")
