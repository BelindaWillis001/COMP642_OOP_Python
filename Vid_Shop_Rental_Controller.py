from Vid_Shop_Customers import Customer
from Vid_Shop_Movies import Movie

class Rental:
    def __init__(self):
        self.allMovies = []
        self.allCustomers = []
        self.rentedMovies = []

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

# define the method to rent a movie
    def RentMovie(self, CustomerName, mname):
        selectedMovie = self.findMovie(mname)
        selectedCustomer = self.findCustomer(CustomerName)
        # Check if the selected movie and customer exist
        if selectedMovie is None:
            print("Movie " + str(selectedMovie) + "not found")
            return
        if selectedCustomer is None:
            print("Customer " + str(selectedCustomer) + "not found")
            return
        # Check if the movie is already rented
        if selectedMovie.MovieRenter != None:
            print(str(selectedMovie.MovieName) + " is already rented")
            return
        # rent the movie and update movie lists
        selectedMovie.MovieRenter = selectedCustomer.CustomerName
        selectedCustomer.rentMovie(selectedMovie)
        print("Movie " + str(selectedMovie.MovieName) + "rented by " + str(selectedCustomer.CustomerName))
        # refresh the list of available movies
        self.AllAvailableMovies()
        # refresh the list of rented movies
        self.AllRentedMovies()

# define the method to return a movie


    def LoadRentalShopData(self):
        # create the objects aMovie and anotherMovie of the class Movie
        firstMovie = Movie('Sisterhood of The Travelling Pants')
        anotherMovie = Movie('The Matrix')
        adifferentMovie = Movie('The Fly')
        # create the objects aCustomer and anotherCustomer of the class Customer
        aCustomer = Customer("Belinda")
        anotherCustomer = Customer("Cindy")
        # create an instance of a Customer renting a movie
        aCustomer.rentMovie(firstMovie)
        # set the movie renter to the customer name
        firstMovie.MovieRenter = aCustomer.CustomerName
        aCustomer.CustomerDetail()
        print(aCustomer.numRentals())
        # create another instance of a Customer renting another movie
        anotherCustomer.rentMovie(anotherMovie)
        # set the movie renter to the customer name
        anotherMovie.MovieRenter = anotherCustomer.CustomerName
        anotherCustomer.CustomerDetail()
        print(anotherCustomer.numRentals())
        # add aCustomer to the Rental Shop
        self.newCustomer(aCustomer)
        self.newCustomer(anotherCustomer)
        print ("the list is " + str(self.allCustomers))
        # add aMovie to the Rental Shop
        self.newMovie(firstMovie)
        self.newMovie(anotherMovie)
        self.newMovie(adifferentMovie)
        print ("the list is " + str(self.allMovies))

# create the loop through to find the movies that haven't been rented
    def AllAvailableMovies(self):
        resultsAvail = []
        for movie in self.allMovies:
            # print a statement to check the movie name and the movie renter
            print(movie.MovieName)
            print(movie.MovieName.MovieRenter)
            if movie.MovieName.MovieRenter == None:
                resultsAvail.append(movie)
        return resultsAvail
# create the loop through to find the movies that have been rented
    def AllRentedMovies(self):
        resultsRented = []
        for movie in self.allMovies:
            print(movie.MovieName)
            print(movie.MovieName.MovieRenter)
            if movie.MovieName.MovieRenter != None:
                resultsRented.append(movie)
        return resultsRented
