import csv
students=[{"rollno":"101","name":"anitha","department":"CSE","mark":86},
          {"rollno":"102","name":"bala","department":"CSE","mark":91},
          {"rollno":"103","name":"chitra","department":"ECE","mark":78}]
course=("python",4)
print("course tuple:",course)
with open("students.txt","w") as file:
    for student in students:
        file.write(str(student)+"\n")
with open("students.csv","w",newline="") as file:
    fields=["rollno","name","department","mark"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
print("\n---records from csv---")
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["rollno"],row["name"],row["department"],row["mark"])
