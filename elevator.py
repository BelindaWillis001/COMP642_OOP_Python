# Define the class (Elevator - cookie cutter)
class Elevator:
    # Define the class constructor
    def __init__(self, currentFloor):
        # Define the class attribute (data, eg currentFloor) - (make the attribute private)
        self.__currentfloor = currentFloor
        # Create the method (function, eg moveUp) - the method is a function that is part of a class, or the behaviour of an object
    def gotoFloor(self, floor):
        # check the floor is between 0 and 6 as there are only 6 floors - and the current floor is not the same as the desired floor
        if 0 <= floor <= 6 and self.__currentfloor != floor:
            # Update the current floor to the desired floor
            self.__currentfloor = floor
        else:
            # Print an error message
            print("Invalid floor request")

    def gotoGround(self):
        # Move the elevator to the ground floor (floor 0)
        self.__currentfloor = 0

    def openDoor(self):
        # Print a message indicating theat the door is opened
        print("Door opened on floor", self.__currentfloor)

    def closeDoor(self):
        # Print a message indicating that the door is closed
        print("Door is closed on floor", self.__currentfloor)

    # add dunder method str to return a printable string
    def __str__(self):
        return "Elevator is on floor " + str(self.__currentfloor)
    
    # Define the getter method to return the current floor
    @property
    def currentfloor(self):
        return self.__currentfloor
    
    # Define the setter method to set the current floor
    @currentfloor.setter
    def currentfloor(self, currentfloor):
        self.__currentfloor = currentfloor

    
# Create the object and declare a variable to reference that specific object (Anelevator - the cookie), initialise the object on floor 6
Anelevator = Elevator(6)

# Move the elevator to floor 4
Anelevator.gotoFloor(4)

# Open the door on floor 4
Anelevator.openDoor()

# Close the door on floor 4
Anelevator.closeDoor()

# Move the elevator to the ground floor
Anelevator.gotoGround()

# Print the current floor of the elevator using the dunder method (str) defined above
print(Anelevator)

# Print the current floor of the elevator
print("Current floor:", Anelevator.currentfloor) 

# print the current floor of the elevator using the getter method
print("Current floor:", Anelevator.currentfloor)

# Set the current floor of the elevator to floor 3 using the setter method
Anelevator.currentfloor = 3

# Print the current floor of the elevator using the getter method
print("Current floor:", Anelevator.currentfloor)
