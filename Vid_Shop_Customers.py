from Vid_Shop_Movies import Movie
# class Customer:
class Customer:
    nextID = 1000
    def __init__(self, cname):
        self.__CustomerID = Customer.nextID
        self.__CustomerName = cname
        self.__CustomerMovies = []
        Customer.nextID += 1
# define the method rentMovie() to add a movie to the list of movies rented by a Customer
    def rentMovie(self, aMovie):
        self.__CustomerMovies.append(aMovie)
# define the method returnMovie() to remove a movie from the list of movies rented by a Customer
    def returnMovie(self, aMovie):
        self.__CustomerMovies.remove(aMovie)
# define the method getRentalsCount() to return the number of movies rented by a Customer
    def numRentals(self):
        return len(self.__CustomerMovies)

# define the getter method for the private attribute __CustomerID
    @property
    def CustomerID(self):
        return self.__CustomerID
# define the getter method for the private attribute __CustomerName
    @property
    def CustomerName(self):
        return self.__CustomerName
# define the setter method for the private attribute __CustomerName
    @CustomerName.setter
    def CustomerName(self, value):
        self.__CustomerName = value
# define the getter method for the private attribute __CustomerMovies
    @property
    def Movies(self):
        return self.__CustomerMovies

    def __str__(self):
        return str(self.__CustomerID) + " " + self.__CustomerName

    def CustomerDetail(self):
        print(self.CustomerName)
        for movie in self.Movies:
            print(movie)

