from Vid_Shop_Movies import Movie
# class Person:
class Person:
    nextID = 1000
    def __init__(self, pname):
        self.__personID = Person.nextID
        self.__personName = pname
        self.__personMovies = []
        Person.nextID += 1
# define the method rentMovie() to add a movie to the list of movies rented by a person
    def rentMovie(self, aMovie):
        self.__personMovies.append(aMovie)
# define the method returnMovie() to remove a movie from the list of movies rented by a person
    def returnMovie(self, aMovie):
        self.__personMovies.remove(aMovie)
# define the method getRentalsCount() to return the number of movies rented by a person
    def numRentals(self):
        return len(self.__personMovies)
    
# define the getter method for the private attribute __personID 
    @property
    def PersonID(self):
        return self.__personID
# define the getter method for the private attribute __personName
    @property
    def PersonName(self,):
        return self.__personName
# define the setter method for the private attribute __personName
    @PersonName.setter
    def PersonName(self, value):
        self.__personName = value
# define the getter method for the private attribute __personMovies
    @property
    def Movies(self):
        return self.__personMovies

    def __str__(self):
        return str(self.__personID) + " " + self.__personName
    
    def personDetail(self):
        print(self.PersonName)
        for movie in self.Movies:
            print(movie)

# create the objects aMovie and anotherMovie of the class Movie
aMovie = Movie('Sisterhood of The Travelling Pants')
anotherMovie = Movie('The Matrix')
print(aMovie)
print(anotherMovie)
# create the objects aPerson and anotherPerson of the class Person
aPerson = Person("Belinda")
anotherPerson = Person("Cindy")
print(aPerson)
print(anotherPerson)
# create an instance of a person renting a movie
aPerson.rentMovie(aMovie)
aPerson.rentMovie(anotherMovie)
aMovie.MovieRenter = "Belinda W"
anotherMovie.MovieRenter = "Belinda W"
aPerson.personDetail()
print(aPerson.numRentals())
# create another instance of a person renting another movie
anotherPerson.rentMovie(anotherMovie)
anotherMovie.__movieRenter = anotherPerson.PersonName
anotherPerson.personDetail()
print(anotherPerson.numRentals())
