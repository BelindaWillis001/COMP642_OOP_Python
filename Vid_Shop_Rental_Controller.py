from Vid_Shop_Customers import Person
from Vid_Shop_Movies import Movie

class Rental:
    def __init__(self):
        self.allMovies = []
        self.allCustomers = []

    def newMovie(self, movieName):
        aMovie = Movie(movieName)
        self.allMovies.append(aMovie)

    def newCustomer(self, customerName):
        aCustomer = Person(customerName)
        self.allCustomers.append(aCustomer)

    def findMovie(self, movieName):
        for movie in self.allMovies:
            if movie.MovieName == movieName:
                return movie
        return None
    
    def findCustomer(self, customerName):
        for customer in self.allCustomers:
            if customer.PersonName == customerName:
                return customer
        return None

    def rentMovie(self, customerName, movieName):
        aMovie = self.findMovie(movieName)
        aPerson = self.findCustomer(customerName)
        print(aMovie)
        print(aPerson)
        print("Previous Renter is " + aMovie.MovieRenter)
        pRenter = aMovie.MovieRenter
        if aMovie.MovieRenter == "None":
            aMovie.MovieRenter = aPerson.PersonName
        else:
            prevRenter = self.findPerson(pRenter)
            print(prevRenter)
            prevRenter.returnMovie(aMovie)
            aMovie.MovieRenter = aPerson.PersonName
        
        print(aMovie.MovieName + " is rented by " + aMovie.MovieRenter)

        aPerson.rentMovie(aMovie)
        print(aPerson.PersonName + " has rented " + str(aPerson.numRentals()) + " movies")

        for person in self.allCustomers:
            person.personDetail()
    
    def returnMovie(self, customerName, movieName):
        aMovie = self.findMovie(movieName)
        aCustomer = self.findCustomer(customerName)
        if aMovie == None:
            print("Movie not found")
            return
        if aCustomer == None:
            print("Customer not found")
            return
        if aMovie.MovieRenter == "None":
            print("Movie not rented")
            return
        aMovie.MovieRenter = "None"
        aCustomer.returnMovie(aMovie)
        print("Movie returned")

    def listMovies(self, customerName):
        myList = ""
        aPerson = self.findCustomer(customerName)

        for movie in aPerson.PersonMovies:
            myList += myList + movie.MovieName + "\n"
        return myList