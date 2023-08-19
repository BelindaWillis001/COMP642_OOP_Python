from Vid_Shop_Customers import Customer
from Vid_Shop_Movies import Movie

class Rental:
    def __init__(self):
        self.allMovies = []
        self.allCustomers = []

    def newMovie(self, mname):
        aMovie = Movie(mname)
        self.allMovies.append(aMovie)
# define the method to add a new customer to the list of customers
    def newCustomer(self, CustomerName):
        aCustomer = Customer(CustomerName)
        self.allCustomers.append(aCustomer)
# define the method to find the movie name to be rented
    def findMovie(self, mname):
        for movie in self.allMovies:
            print(movie.MovieName)
            if movie.MovieName == mname:
                return movie
        return None
# define the method to find the customer name
    def findCustomer(self, CustomerName):
        for customer in self.allCustomers:
            print(customer.CustomerName)
            if customer.CustomerName == CustomerName:
                return customer
        return None



    def rentMovie(self, CustomerName, mname):
        selectedMovie = self.findMovie(mname)
        selectedCustomer = self.findCustomer(CustomerName)
        selectedCustomer.rentMovie(selectedMovie)

    

    def LoadRentalShopData(self):
        # create the objects aMovie and anotherMovie of the class Movie
        aMovie = Movie('Sisterhood of The Travelling Pants')
        anotherMovie = Movie('The Matrix')
        anunrentedMovie = Movie('The Fly')
        # create the objects aCustomer and anotherCustomer of the class Customer 
        aCustomer = Customer("Belinda")
        anotherCustomer = Customer("Cindy")
        # create an instance of a Customer renting a movie
        aCustomer.rentMovie(aMovie)
        aMovie.MovieRenter = aCustomer.CustomerName
        aCustomer.CustomerDetail()
        print(aCustomer.numRentals())
        # create another instance of a Customer renting another movie
        anotherCustomer.rentMovie(anotherMovie)
        anotherMovie.MovieRenter = anotherCustomer.CustomerName
        anotherCustomer.CustomerDetail()
        print(anotherCustomer.numRentals())
        # add aCustomer to the Rental Shop
        self.newCustomer(aCustomer)
        self.newCustomer(anotherCustomer)
        print ("the list is " + str(self.allCustomers))
        # add aMovie to the Rental Shop
        self.newMovie(aMovie)
        self.newMovie(anotherMovie)
        self.newMovie(anunrentedMovie)
        print ("the list is " + str(self.allMovies))

