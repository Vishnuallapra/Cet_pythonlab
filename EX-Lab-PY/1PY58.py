class Student:
    def getStudentDetails(self):
        self.rollno_58=input("\nEnter Roll Number : ")
        self.name_58 = input("Enter Student Name : ")
        self.course_58 =input("Enter Course : ")
        self.mark1_58 = int(input("Enter Mark1 : "))
        self.mark2_58 = int(input("Enter Mark2 : "))
        
    def printResult(self):
        print("Roll No:",self.rollno_58)
        print("Name :",self.name_58)
        print("Course:",self.course_58)
        print("Total Mark :",self.mark1_58+self.mark2_58)

        
S1_58=Student()
S1_58.getStudentDetails()
S2_58=Student()
S2_58.getStudentDetails()
S3_58=Student()
S3_58.getStudentDetails()

print("\n")

S1_58.printResult()
S2_58.printResult()
S3_58.printResult()