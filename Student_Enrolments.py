class student:
    def __init__(self, ID, firstName, lastName = "unknown"):
        self.studentID = ID
        self.studentFirstname = firstName
        self.studentLastname = lastName
    def __str__(self):
        return ("Student ID: {} Name: {} {}".format(self.studentID, self.studentFirstname, self.studentLastname))

Person1 = student("1", "Sarah")
Person2 = student("2", "Scott", "Willis")
Person3 = student("3", "Belinda", "Willis")

studentList = []

# Define a method to add a new person to myStudents list.
def addPerson(aPerson, aList):
    aList.append(aPerson)

# add students to the list of myStudents using the method addPerson
addPerson(Person1, studentList)
addPerson(Person2, studentList)
addPerson(Person3, studentList)


class enrolment:
    def __init__(self):
        self.studentList = []
    def __str__(self):
        return ("Enrolments are:" (self.studentList))
    
print(studentList)