import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Vid_Shop_Rental_Controller import Rental


company = Rental()

# Define a read data method to produce the list of customers and movies
def btnReadData():
    company.LoadRentalShopData()
    for customer in company.allCustomers:
        lstbox_ppl.insert(tk.END, customer.CustomerName)

    for movie in company.AllAvailableMovies():
        lstbox_moviesA.insert(tk.END, movie.MovieName)

    for movie in company.AllRentedMovies():
        lstbox_moviesR.insert(tk.END, movie.MovieName)


# Define a method to rent a movie
def btnRentMovie():
    # get the customer
    selCustomerIndex = lstbox_ppl.curselection()
    selectedCustomer = lstbox_ppl.get(selCustomerIndex)

    # get the movie
    selMovieIndex = lstbox_moviesA.curselection()
    selectedMovie = lstbox_moviesA.get(selMovieIndex)

    # rent the movie
    company.RentMovie(str(selectedCustomer), str(selectedMovie))

# define a method for an already rented movie
def btnReturnMovie():
    # get the selected movie
    selMovieIndex = lstbox_moviesR.curselection()
    selectedMovie = lstbox_moviesR.get(selMovieIndex)

    # get the selected customer
    selCustomerIndex = lstbox_ppl.curselection()
    selectedCustomer = lstbox_ppl.get(selCustomerIndex)

    # return the movie
    company.returnMovie(str(selectedCustomer), str(selectedMovie))
    


# Create a window
root = tk.Tk()
root.geometry("1200x400")
root.config(background = "#ffffff")

# Create a title
root.title('My Video Store App')

# define a method called button clicked
def button_clicked():
    print("I was clicked!")

# place a label to the root window
lblHello = ttk.Label(root, text="Welcome to my Video Store App")
lblHello.pack()

# place a button
btnClick = ttk.Button(root, text="Read Video Shop Database", command = btnReadData)
btnClick.pack()

# add the widgets
frm_formDisp = tk.Frame(relief=tk.FLAT, borderwidth=3)

# pack the frame into the window
frm_formDisp.pack(padx=25, pady=25)

lbl_ppl_title = tk.Label(master=frm_formDisp, text="Customers")
lbl_ppl_title.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lstbox_ppl = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE, width=0)
lstbox_ppl.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lbl_movies_titleA = tk.Label(master=frm_formDisp, text="Available Movies")
lbl_movies_titleA.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lstbox_moviesA = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE, width=0)
lstbox_moviesA.pack(fill='x', padx=20, pady=5,side=tk.LEFT)
#  sets the frame around the button and the location of the button
frm_button_rent = tk.Frame(relief=tk.FLAT, borderwidth=3)
frm_button_rent.pack(padx=20, pady=5, side=tk.TOP)
# sets the padding around the button width
button_rent = ttk.Button(master=frm_button_rent, text="Rent Movie", command=btnRentMovie)
button_rent.pack(padx=5, pady=5)

lbl_moviesR_title = tk.Label(master=frm_formDisp, text="Rented Movies")
lbl_moviesR_title.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lstbox_moviesR = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE, width=0)
lstbox_moviesR.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

frm_button_return = tk.Frame(relief=tk.FLAT, borderwidth=3)
frm_button_return.pack(padx=20, pady=5, side=tk.TOP)

button_return = ttk.Button(master=frm_button_return, text="Return Movie", command=btnReturnMovie)
button_return.pack(padx=5, pady=5)

root.mainloop()