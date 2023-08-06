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
        # Define the Member attributes
        self.memberFirstname = firstname
        self.memberLastname = lastname
        self.memberID = memberID
        # create an empty list to store the classes that the member is enrolled in
        self.memberClassList = []
    # Define the Dunder method to return a printable string of Member attributes
    def __str__(self):
        return ("Member Name: {} {} Member ID: {}".format(self.memberFirstname, self.memberLastname, self.memberID))
    # Define a method to return the classes the member is enrolled in
    def getMemberClasses(self):
        return self.memberClassList
    # Define a method to allow a member to cancel their enrolment in a class
    def removeClass(self, aClass):
        self.memberClassList.remove(aClass)
    # Define a method to allow a member to enrol in a class
    def addClass(self, aClass):
        self.memberClassList.append(aClass)


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
    def addtrainerClass(self, aClass):
        self.trainerClasses.append(aClass)

# Create the Trainer (objects) - cookies
trainer1 = Trainer("Sayaka", "Kanayma", "Yoga")
trainer2 = Trainer("Emma", "McConnell", "Pilates")

print(trainer1)
print(trainer2)


    
    # Create the exercise classes (objects) - cookie
exerciseclass1 = GroupExercise("Yoga", "Sayaka", 25, 15.00)
exerciseclass2 = GroupExercise("Pilates", "Emma", 4, 30.00)

print(exerciseclass1)
print(exerciseclass2)

# Create the member (objects) - cookies
member1 = Member("Sarah", "Lind", "1")
member2 = Member("Scott", "Willis", "2")
member3 = Member("Belinda", "Allison", "3")
member4 = Member("Peter", "Dunn", "4")
member5 = Member("Cassie", "Lieu", "5")
    
print(member1)
print(member2)
print(member3)
print(member4)
print(member5)


# call the add class method on the member object to add a class to the member's list of classes
member1.addClass(exerciseclass1)
member1.addClass(exerciseclass2)
# print out the class details for all the classes the member is enrolled in
for aClass in member1.getMemberClasses():
    print(aClass.classDetails())


# call the add trainer class method on the trainer object to add a class to the trainer's list of classes
trainer1.addtrainerClass(exerciseclass1)
trainer2.addtrainerClass(exerciseclass2)
trainer1.addtrainerClass(exerciseclass2)
# print out the class details for all the classes the trainer teaches
for Classes in trainer1.getTrainerClasses():
    print()