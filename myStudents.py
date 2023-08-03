# Define the class of Student (the cookie cutter)
class Student:
    def __init__(self, firstName, lastName, age):
        self.firstname = firstName
        self.lastname = lastName
        self.Age = age
    def __str__(self):
        return self.firstname + " " + self.lastname + " is " + str(self.Age)
    def speak(self):
        print("Hello, my name is ", self.firstname, " ", self.lastname, " and I am ", self.Age, " years old.")

# Define the object of a Student (the cookie)
Person0 = Student("Belinda", "Willis", 54)
Person1 = Student("Cassie", "Lieu", 35)
Person2 = Student("Sarah", "Lind", 23)
Person3 = Student("John", "Strange", 62)
# Create a list of my students
myStudents = []
# Define a method to add a new person to myStudents list.
def addPerson(aPerson, aList):
    aList.append(aPerson)

# Create a list of my students
myotherStudents = []
myotherStudents.append(Person3)
myotherStudents.append(Person2)


# add students to the list of myStudents using the method addPerson
addPerson(Person0, myStudents)
addPerson(Person1, myStudents)
addPerson(Person2, myStudents)
addPerson(Person3, myStudents)

# Print the length of the myStudents list
print(len(myStudents))

# Print the length of the myotherStudents list
print(len(myotherStudents))

# # Remove a person from myStudents list from index 2 (Sarah Lind).
# myStudents.pop(2)


# # Define the method to print a list
def displayRowdata(anylist):
    for row in anylist:
        print(row)


# # Call the method to print the list of students
displayRowdata(myStudents)
displayRowdata(myotherStudents)

# Define the old students with hard coded age
def dispOldstudents():
    for student in myStudents:
        if student.Age > 30:
            print("The name of the older student: " + student.firstname + " " + "(hard-coded age)")
dispOldstudents()

# Define the old students with age as a parameter
def dispOldstudents(anAge):
    for student in myStudents:
        if student.Age > anAge:
            print("The name of the older student: " + student.firstname + " " + "(age as a parameter)")
dispOldstudents(50)

# Define the number of old students using count method with age as a parameter of the method countOldstudents
def countOldstudents(anAge):
    count = 0
    for student in myStudents:
        if student.Age > anAge:
            count += 1
    return count

print("The number of old students is: ", countOldstudents(50))

# print the names of students that are in both lists
def printCommonStudents():
    for student in myStudents:
        for otherstudent in myotherStudents:
            if student == otherstudent:
                print(student.firstname + " " + student.lastname + " is in both student lists.")
printCommonStudents()