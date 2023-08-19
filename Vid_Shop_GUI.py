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

    for movie in company.allMovies:
        lstbox_movies.insert(tk.END, movie.MovieName)


# Define a method to rent a movie
def btnRentMovie():
    # get the customer
    selCustomerIndex = lstbox_ppl.curselection()
    selectedCustomer = lstbox_ppl.get(selCustomerIndex)

    # get the movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    # rent the movie
    company.rentMovie(str(selectedCustomer), str(selectedMovie))

# define a method for an already rented movie
def btnReturnMovie():
    # get the selected movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    # get the selected customer
    selCustomerIndex = lstbox_ppl.curselection()
    selectedCustomer = lstbox_ppl.get(selCustomerIndex)

    # return the movie
    company.returnMovie(str(selectedCustomer), str(selectedMovie))
    


# Create a window
root = tk.Tk()
root.geometry("800x400")
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

lstbox_ppl = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE, width=30)
lstbox_ppl.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lbl_movies_title = tk.Label(master=frm_formDisp, text="Movies")
lbl_movies_title.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lstbox_movies = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE, width=60)
lstbox_movies.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

frm_formButton = tk.Frame(relief=tk.FLAT, borderwidth=3)

# Pack the frame into the window
frm_formButton.pack()

# button
button1 = ttk.Button(master=frm_formButton, text="Rent Movie", command=btnRentMovie)
button1.pack(fill='x', padx=5, pady=5,side=tk.LEFT)

button2 = ttk.Button(master=frm_formButton, text="Return Movie", command=btnReturnMovie)
button2.pack(fill='x', padx=5, pady=5,side=tk.LEFT)

root.mainloop()