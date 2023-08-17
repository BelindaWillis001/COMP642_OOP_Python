import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Vid_Shop_Rental_Controller import Rental

company = Rental()

# Define a read data method
def btnReadData():
    for i in range(1, 3):
        lstbox_ppl.insert(tk.END, "PERSON" + str(i))
        company.newPerson("PERSON" + str(i))

    for j in range(1, 3):
        lstbox_movies.insert(tk.END, "MOVIE" + str(j))
        company.newMovie("MOVIE" + str(j))

# Define a method to rent a movie
def btnRentMovie():
    # get the person
    selPersonIndex = lstbox_ppl.curselection()
    selectedPerson = lstbox_ppl.get(selPersonIndex)

    # get the movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    # rent the movie
    company.rentMovie(str(selectedPerson), str(selectedMovie))

# define a method for an already rented movie
def btnWhoHasTheMovie():
    # get the selected movie
    selMovieIndex = lstbox_movies.curselection()
    selectedMovie = lstbox_movies.get(selMovieIndex)

    # get the person who has the movie
    theRenter = company.whoHasTheMovie(str(selectedMovie))
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
btnClick = ttk.Button(root, text="Click Me", command = button_clicked)
btnClick.pack()

# add the widgets
frm_formDisp = tk.Frame(relief=tk.FLAT, borderwidth=3)

# pack the frame into the window
frm_formDisp.pack(padx=25, pady=25)

# pack the frame into the window

root.mainloop()