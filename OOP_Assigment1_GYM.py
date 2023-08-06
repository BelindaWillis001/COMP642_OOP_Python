# Define the class GroupExercise (cookie cutter)
class GroupExercise:
# Define the class constructor
    def __init__(self, name, trainer, capacity, fee):
        # Define the attributes
        self.className = name
        self.classTrainer = trainer
        self.classCapacity = capacity
        self.classFee = fee
        # create an empty list to store the participants in the class
        self.classParticipants = []
        # create an empty list to store the waitlist for the class
        self.classWaitlist = []
        # create an empty list to store the participants who have checked in to the class
        self.classCheckedin = []
    # Define a method that prints out the details of the class (not using Dunder Method)
    def classDetails(self):
        return ("Class = " + self.className + ", Teacher = " + self.classTrainer+ ", Max No = " + str(self.classCapacity)+ ", Cost =  " + str(self.classFee))
    # Define the Dunder method prints out the details of the class
    def __str__(self):
        return ("Class Name: {} Trainer: {} Capacity: {} Fee: {}".format(self.className, self.classTrainer, self.classCapacity, self.classFee))
    # Define a method to return the participants in the class
    def getClassParticipants(self):
        return self.classParticipants
    # Define a method to return the waitlist for the class
    def getClassWaitlist(self):
        return self.classWaitlist
    # Define a method to return the participants who have checked in to the class
    def getClassCheckedin(self):
        return self.classCheckedin
    
    
#Define the class Member (cookie cutter) 
class Member:
    # Define the Member class constructor
    def __init__(self, firstname, lastname, memberID):
        # Define the Member attributes (make them private attributes)
        self.__memberFirstname = firstname  
        self.__memberLastname = lastname
        self.__memberID = memberID
        # create an empty list to store the classes that the member is enrolled in
        self.memberClassList = []
# Define the private method to display the member's details
    def __display(self):
        print("This is a private method")
    # Define a getter method to return the member's details from the private attributes
    @property
    def memberDetails(self):
        print("This is getting the member details from the private setting....")
        return self.__memberFirstname + " " + self.__memberLastname + " " + self.__memberID
    
    # Define a setter method to set the member's details from the private attributes
    @memberDetails.setter
    def memberDetails(self, memberDetails):
        print("This is setting the member details from the private setting....")
        self.__memberFirstname, self.__memberLastname, self.__memberID = memberDetails.split(" ")

    # Define the Dunder method to return a printable string of Member attributes
    def __str__(self):
        return ("Member Name: {} {} Member ID: {}".format(self.__memberFirstname, self.__memberLastname, self.__memberID))
    # Define a method to return the classes the member is enrolled in
    def getMemberClasses(self):
        return self.memberClassList
    # Define a method to allow a member to cancel their enrolment in a class
    def removeClass(self, classToRemove):
        self.memberClassList.remove(classToRemove)
    # Define a method to allow a member to enrol in a class
    def addClass(self, classToAdd):
        self.memberClassList.append(classToAdd)


# Define the class Trainer (cookie cutter)
class Trainer:
    def __init__(self, firstname, lastname, specialisation):
        self.trainerFirstname = firstname
        self.trainerLastname = lastname
        self.trainerSpecialty = specialisation
        # create an empty list to store the classes that the trainer teaches
        self.trainerClasses = []
    # Define the Dunder method to return a printable string of Trainer attributes
    def __str__(self):
        return ("Trainer Name: {} {} Specialty: {}".format(self.trainerFirstname, self.trainerLastname, self.trainerSpecialty))
    # Define a method to return the classes the trainer teaches
    def getTrainerClasses(self):
        return self.trainerClasses
    # Define a method to allow a trainer to add a class to their list of classes they teach
    def addTrainerClass(self, classToAdd):
        self.trainerClasses.append(classToAdd)

# Create the Trainer (objects) - cookies
trainer1 = Trainer("Sayaka", "Kanayma", "Yoga")
trainer2 = Trainer("Emma", "McConnell", "Pilates")

# print(trainer1)
# print(trainer2)


    
    # Create the exercise classes (objects) - cookie
exerciseclass1 = GroupExercise("Yoga", "Sayaka", 25, 15.00)
exerciseclass2 = GroupExercise("Pilates", "Emma", 4, 30.00)

# print(exerciseclass1.classDetails())
# print(exerciseclass2.classDetails())

# Create the member (objects) - cookies
member1 = Member("Sarah", "Lind", "1")
member2 = Member("Scott", "Willis", "2")
member3 = Member("Belinda", "Allison", "3")
member4 = Member("Peter", "Dunn", "4")
member5 = Member("Cassie", "Lieu", "5")
    
print(member2.memberDetails)
member2.memberDetails = "Scott Allison 2"

print(member2.memberDetails)


# call the add class method on the member object to add a class to the member's list of classes
member1.addClass(exerciseclass1)
member1.addClass(exerciseclass2)
member2.addClass(exerciseclass1)
member3.addClass(exerciseclass2)

# print out the class details for all the classes the member is enrolled in
# for aClass in member1.getMemberClasses():
#     print(aClass.classDetails())

# for aClass in member2.getMemberClasses():
#     print(aClass.classDetails())


# call the add trainer class method on the trainer object to add a class to the trainer's list of classes
trainer1.addTrainerClass(exerciseclass1)
trainer2.addTrainerClass(exerciseclass2)
trainer1.addTrainerClass(exerciseclass2)
# print out the class details for all the classes the trainer teaches
# for Classes in trainer1.getTrainerClasses():
#     print(Classes.classDetails())