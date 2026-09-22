import csv

def get_grade(marks):
    if marks>=90:
        grade="A+"
    elif marks>=80:
        grade="A"
    elif marks>=70:
        grade="B"
    elif marks>=60:
        grade="C"  
    else:
        grade="Fail" 
    return grade
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    print("STUDENT REPORT MANAGER")
    print("-"*40)
    print(f"{'Name':<20}{'Marks':<10}{'Grade':<8}")
    print("-"*40)

    all_marks=[]  
    for line in csv_reader:
        marks=int(line['marks'])
        grade=get_grade(marks) 
        all_marks.append(marks)
        print(f"{line['name']:<20}{marks:<10}{grade:<8}")  
    print("-"*40) 
    print(f"{'Average Marks'}:{sum(all_marks)/len(all_marks):.2f}") 
    print(f"{'Highest Marks'}:{max(all_marks):}")  
    print(f"{'Lowest Marks'}:{min(all_marks):}")
    print(f"{'Total Students'}:{len(all_marks)}")      
