import tkinter as tk
import backend
import sys

# Naming color hexcodes
# Taken from Gruvbox Dark theme
bg0 = "#282828"
bg1 = "#3c3836"
bg2 = "#504945"
bg3 = "#665c54"
fg1 = "#ebdbb2"
gruvYellow = "#d79921"  # Called gruv yellow as yellow is already a system color

def product_table():
    # Product table menu
    createButton = tk.Button(text="(Re)Create Product Table", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.create_product_table_UI).pack()
    addButton = tk.Button(text="Add new product", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=backend.insert_UI).pack()
    updateButton = tk.Button(text="Update existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.update_UI).pack()
    deleteButton = tk.Button(text="Delete existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.delete_UI).pack()
    findButton = tk.Button(text="Find products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.select_products_UI).pack()
    listButton = tk.Button(text="List products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.list_products_UI).pack()
    exitButton = tk.Button(text="Exit", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=sys.exit).pack()

def login():
    inp = loginPassword.get()
    if inp != "password":
        wrongPassword.configure(text="Wrong password!")
    else:
        loginWindow.destroy()
        window = tk.Tk()
        window.title("Davis\' Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 2.0)  # Makes all widgets 2x as big.
        window.configure(background=bg1)
        product_table()

#FIRST WINDOW
loginWindow = tk.Tk()
loginWindow.title("Davis\' Coffee Shop Database")
loginWindow.geometry("800x600")
loginWindow.tk.call('tk', 'scaling', 2.0)  # Makes all widgets 2x as big.
loginWindow.configure(background=bg1)  # Changes background color

loginPassword = tk.Entry(fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
loginButton = tk.Button(text="Login", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=login)
wrongPassword = tk.Label(text="", fg=fg1, bg=bg1) #placeholder for wrong password label

loginPassword.pack()
loginButton.pack()
wrongPassword.pack()

loginWindow.mainloop()
