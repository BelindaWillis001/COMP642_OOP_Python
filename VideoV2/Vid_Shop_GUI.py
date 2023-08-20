import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Vid_Shop_Rental_Controller import Rental

company = Rental()

# Define a read data method
def btnReadData():
    for i in range(1, 3):
        lstbox_ppl.insert(tk.END, "CUSTOMER" + str(i))
        company.newCustomer("CUSTOMER" + str(i))

    for j in range(1, 3):
        lstbox_movies.insert(tk.END, "MOVIE" + str(j))
        company.newMovie("MOVIE" + str(j))

# Define a method to rent a movie
def btnRentMovie():
    # get the customer
    selCustomerIndex = lstbox_ppl.curselection()
    selectedCustomer = lstbox_ppl.get(selCustomerIndex)

    # get the movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    print(selectedCustomer + " " + selectedMovie)
    # rent the movie
    company.RentMovie(str(selectedCustomer), str(selectedMovie))

# define a method for an already rented movie
def btnMovieRenter():
    # get the selected movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    # get the customer who has the movie
    theRenter = company.MovieRenter(str(selectedMovie))
    showinfo(title="Info", message= theRenter)


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
btnClick = ttk.Button(root, text="Click Me", command = btnReadData)
btnClick.pack()

# add the widgets
frm_formDisp = tk.Frame(relief=tk.FLAT, borderwidth=3)

# pack the frame into the window
frm_formDisp.pack(padx=25, pady=25)

lstbox_ppl = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE)
lstbox_ppl.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

lstbox_movies = tk.Listbox(master=frm_formDisp, exportselection=0, selectmode=tk.BROWSE)
lstbox_movies.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

frm_formButton = tk.Frame(relief=tk.FLAT, borderwidth=3)

# Pack the frame into the window
frm_formButton.pack()

# button
button1 = ttk.Button(master=frm_formButton, text="Rent Movie", command=btnRentMovie)
button1.pack(fill='x', padx=5, pady=5,side=tk.LEFT)

button2 = ttk.Button(master=frm_formButton, text="Who Has The Movie", command=btnMovieRenter)
button2.pack(fill='x', padx=5, pady=5,side=tk.LEFT)

root.mainloop()