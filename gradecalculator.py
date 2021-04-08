class Student:
    def getStudentDetails(self):
        self.name = input("Enter The Name Of Student: ")
        self.assignment = list(map(int,input("Enter The Assignment Marks: ").strip().split()))
        self.test = list(map(int,input("Enter The Test Marks: ").strip().split()))
        self.labwork = list(map(int,input("Enter The Labwork Marks: ").strip().split()))
    def display(self):
        show = ({"Name" : self.name,
               "Assignment" : self.assignment,
               "Test" : self.test,
               "Labwork" : self.labwork})
        return show
#Function to calculate average
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum/len(marks)
#Functionto calculate total average
def cal_tot_avg(students):
    assignment = get_average(students["Assignment"])
    test = get_average(students["Test"])
    lab = get_average(students["Labwork"])
    #Return result based on weightage
    return(0.1*assignment + 0.7*test +0.2*lab)
#Calculate grade
def grade(score):
    if score >= 90 : return"A"
    elif score >= 80 : return"B"
    elif score >= 70 : return"C"
    elif score >= 60 : return"D"
    else : return"E"
#Function to calculate total avg of whole class
def class_avg(student_list):
    result_list = []
    for student in student_list:
        stud_avg = cal_tot_avg(student)
        result_list.append(stud_avg)
        return get_average(result_list)
#Student list constiting the dictionary of all students
s1 = Student()
s1.getStudentDetails()
a = s1.display()
s2 = Student()
s2.getStudentDetails()
b = s2.display()
s3 = Student()
s3.getStudentDetails()
c = s3.display()
students = [a,b,c]
for i in students:
    print(i["Name"])
    print("Average marks of %s is : %s" %(i["Name"], cal_tot_avg(i)))
    print("Grade of %s is : %s" %(i["Name"],grade(cal_tot_avg(i))))
    print()
#Calculate the average of whole class
class_average = class_avg(students)

print("Class Average is %s "%(class_average))
print("Grade of the Class is %s "%(grade(class_average)))
