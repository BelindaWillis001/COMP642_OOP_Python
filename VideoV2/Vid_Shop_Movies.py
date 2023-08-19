class Movie:
    def __init__(self, mname):
        self.__movieName = mname
        self.__movieRenter = "None"
        self.__movieReturn = None
        self.__movieRentFee = None
    # define the getter method for the private attribute __movieName 
    @property
    def MovieName(self):
        return self.__movieName
    #  define the setter method for the private attribute __movieName
    @MovieName.setter
    def MovieName(self, value):
        self.__movieName = value
    # define the getter method for the private attribute __movieRenter
    @property
    def MovieRenter(self):
        return self.__movieRenter
    # define the setter method for the private attribute __movieRenter
    @MovieRenter.setter
    def MovieRenter(self, value):
        self.__movieRenter = value
    
    def __str__(self):
        return self.__movieName + " " + self.__movieRenter
    # define the equality method for the class Movie which compares the 
    # movie names of two movies and returns True if they are the same 
    def __eq__(self, other):
        return self.__movieName == other.__movieName