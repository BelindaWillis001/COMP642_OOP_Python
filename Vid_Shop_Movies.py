class Movie:
    def __init__(self, movieName):
        self.__movieName = movieName
        self.__movieRenter = "None"
        self.__movieReturn = None
        self.__movieRentFee = None
    
    @property
    def MovieName(self):
        return self.__movieName
    
    @MovieName.setter
    def MovieName(self, value):
        self.__movieName = value
    
    @property
    def MovieRenter(self):
        return self.__movieRenter
    
    @MovieRenter.setter
    def MovieRenter(self, value):
        self.__movieRenter = value
    
    def __str__(self):
        return self.__movieName + " " + self.__movieRenter
    # define the equality method for the class Movie which compares the 
    # movie names of two movies and returns True if they are the same 
    def __eq__(self, other):
        return self.__movieName == other.__movieName