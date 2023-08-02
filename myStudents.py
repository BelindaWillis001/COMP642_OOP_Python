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
myStudents.append(Person0)
myStudents.append(Person1)
myStudents.append(Person3)

# Create a list of my students
myotherStudents = []
myotherStudents.append(Person3)
myotherStudents.append(Person2)

# Define a method to add a new person to myStudents list.
myStudents.insert(1, Person2)

# Print the length of the myStudents list
print(len(myStudents))

# Print the length of the myotherStudents list
print(len(myotherStudents))

# Define a method to remove a person from myStudents list.
myStudents.pop(1)
# Define a method to add a new person to myStudents list.
myStudents.append(Person2)

# # Define the method to print the list of students
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
            print(student.firstname)
dispOldstudents()

# Define the old students with age as a parameter
def dispOldstudents(anAge):
    for student in myStudents:
        if student.Age > anAge:
            print(student.firstname)
dispOldstudents(40)

# Define the number of old students using count method
def countOldstudents(anAge):
    count = 0
    for student in myStudents:
        if student.Age > anAge:
            count += 1
    return count

print("The number of old students is: ", countOldstudents(20))