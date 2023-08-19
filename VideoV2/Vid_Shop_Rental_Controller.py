from Vid_Shop_Customers import Customer
from Vid_Shop_Movies import Movie

class Rental:
    def __init__(self):
        self.allMovies = []
        self.allCustomers = []

    def newMovie(self, mname):
        aMovie = Movie(mname)
        self.allMovies.append(aMovie)

    def newCustomer(self, CustomerName):
        aCustomer = Customer(CustomerName)
        self.allCustomers.append(aCustomer)

    def findMovie(self, mname):
        for movie in self.allMovies:
            if movie.MovieName == mname:
                return movie
        return None
    
    def findCustomer(self, CustomerName):
        for customer in self.allCustomers:
            print(customer.CustomerName)
            if customer.CustomerName == CustomerName:
                return customer
        return None
    
    def MovieRenter(self, CustomerName, mname):
        aMovie = self.findMovie(mname)
        aCustomer = self.findCustomer(CustomerName)
        print(aMovie)
        print(aCustomer)
        print("Previous Renter is " + aMovie.MovieRenter)
        MovieRenter = aMovie.MovieRenter
        if aMovie.MovieRenter == "None":
            aMovie.MovieRenter = aCustomer.CustomerName
        else:
            return aMovie.MovieRenter

    def rentMovie(self, CustomerName, mname):
        aMovie = self.findMovie(mname)
        aCustomer = self.findCustomer(CustomerName)

        if aMovie is None:
            print("Movie not found")
            return
        
        if aCustomer is None:
            print("Customer not found")
            return 
        
        if aMovie.MovieRenter != "None":
            print("Movie already rented")
            return
        
        # the movie is available for rent
        aMovie.MovieRenter = aCustomer.CustomerName
        #add the movie to the customer's movie's list

        # print("Previous Renter is " + aMovie.MovieRenter)
        # pRenter = aMovie.MovieRenter
        # if aMovie.MovieRenter == "None":
        #     aMovie.MovieRenter = aCustomer.CustomerName
        # else:
        #     prevRenter = self.findCustomer(pRenter)
        #     print(prevRenter)
        #     prevRenter.returnMovie(aMovie)
        #     aMovie.MovieRenter = aCustomer.CustomerName

        aCustomer.rentMovie(aMovie)
        print(aCustomer.CustomerName + " has rented " + str(aCustomer.numRentals()) + " movies")
    
    def returnMovie(self, CustomerName, mname):
        aMovie = self.findMovie(mname)
        aCustomer = self.findCustomer(CustomerName)
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

    def listMovies(self, CustomerName):
        myList = ""
        aCustomer = self.findCustomer(CustomerName)

        for movie in aCustomer.CustomerMovies:
            myList += myList + movie.MovieName + "\n"
        return myList
    

videoShop = Rental()

videoShop.newCustomer('customer1')
videoShop.newMovie('movie1')
videoShop.newCustomer('customer2')
videoShop.newMovie('movie2')

print(len(videoShop.allMovies))
print(len(videoShop.allCustomers))

print(videoShop.findCustomer("customer1"))
print(videoShop.findMovie("movie1"))

videoShop.rentMovie('customer1', 'movie1')
print("End")