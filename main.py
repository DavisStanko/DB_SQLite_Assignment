#fix no button pls
import sqlite3
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


def create_product_table_UI():
    def no():
        global window
        createWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        product_table()
        
    def yes():
        global messageLabel
        db_name = "davis\'coffee_shop.db"
        sql = """create table Product
                (ProductID integer,
                Name text,
                Price real,
                primary key(ProductID))"""
        table_name = "Product"

        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute(
                "select name from sqlite_master where name=?", (table_name,))
            result = cursor.fetchall()
            keep_table = True
            if len(result) == 1:
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
            else:
                keep_table = False

            # create the table if required (not keeping old one)
            if not keep_table:
                cursor.execute(sql)
                db.commit()
        no()
        messageLabel.configure(text="Table created!")
        


    global window
    window.destroy()
    createWindow = tk.Tk()
    createWindow.title("(Re)Create Product Table")
    createWindow.geometry("800x600")
    createWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
    createWindow.configure(background=bg1)
    createWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    confirmLabel = tk.Label(createWindow, text="This action will overwrite any prexisting database with the same name,\nare you sure you would like to continue?", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0",)
    yesButton = tk.Button(createWindow, text="Yes", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(createWindow, text="No", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

    confirmLabel.grid(row=0, column=0, padx=10, pady=10)
    confirmLabel.grid_columnconfigure(1, weight=1)
    yesButton.grid(row=1, column=0, padx=10, pady=10)
    yesButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=6, column=0, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)

def insert_UI():
    def no():
        global window
        insertWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        product_table()
        
    def yes():
        inpProduct = productEntry.get()  # Get text field contents
        inpCost = costEntry.get()  # Get text field contents
        if inpProduct == "" or inpCost == "":
            errorLabel.configure(text="Please fill in both inputs!")
        else:
            no()
            messageLabel.configure(text="Item added!")
        


    global window
    window.destroy()
    insertWindow = tk.Tk()
    insertWindow.title("(Add to Product Table")
    insertWindow.geometry("800x600")
    insertWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
    insertWindow.configure(background=bg1)
    insertWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(insertWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    productPromptLabel = tk.Label(insertWindow, text="Product Name:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    costPromptLabel = tk.Label(insertWindow, text="Cost:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    productEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    costEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    yesButton = tk.Button(insertWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(insertWindow, text="Cancel", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

    errorLabel.grid(row=0, column=0, padx=10, pady=10)
    
    productPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    productPromptLabel.grid_columnconfigure(1, weight=1)
    costPromptLabel.grid(row=2, column=0, padx=10, pady=10)
    costPromptLabel.grid_columnconfigure(1, weight=1)
    productEntry.grid(row=1, column=1, padx=10, pady=10)
    productEntry.grid_columnconfigure(1, weight=1)
    costEntry.grid(row=2, column=1, padx=10, pady=10)
    costEntry.grid_columnconfigure(1, weight=1)
    yesButton.grid(row=3, column=0, padx=10, pady=10)
    yesButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=3, column=1, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)

def product_table():
    global messageLabel
    # Product table menu
    messageLabel = tk.Label(window, text="", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    createButton = tk.Button(window, text="(Re)Create Product Table", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=create_product_table_UI)
    addButton = tk.Button(window, text="Add new product", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=insert_UI)
    updateButton = tk.Button(window, text="Update existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.update_UI)
    deleteButton = tk.Button(window, text="Delete existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.delete_UI)
    findButton = tk.Button(window, text="Find products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.select_products_UI)
    listButton = tk.Button(window, text="List products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backend.list_products_UI)
    exitButton = tk.Button(window, text="Exit", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=sys.exit)

    messageLabel.grid(row=0, column=0, padx=10, pady=10)
    messageLabel.grid_columnconfigure(1, weight=1)
    createButton.grid(row=1, column=0, padx=10, pady=10)
    createButton.grid_columnconfigure(1, weight=1)
    addButton.grid(row=2, column=0, padx=10, pady=10)
    addButton.grid_columnconfigure(1, weight=1)
    updateButton.grid(row=3, column=0, padx=10, pady=10)
    updateButton.grid_columnconfigure(1, weight=1)
    deleteButton.grid(row=4, column=0, padx=10, pady=10)
    deleteButton.grid_columnconfigure(1, weight=1)
    findButton.grid(row=5, column=0, padx=10, pady=10)
    findButton.grid_columnconfigure(1, weight=1)
    listButton.grid(row=6, column=0, padx=10, pady=10)
    listButton.grid_columnconfigure(1, weight=1)
    exitButton.grid(row=7, column=0, padx=10, pady=10)
    exitButton.grid_columnconfigure(1, weight=1)


def login():
    global window
    inp = loginPassword.get()  # Get text field contents
    if inp == "password":
        loginWindow.destroy()
        window = tk.Tk()
        window.title("Davis\' Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        product_table()
    else:
        wrongPassword.configure(text="Wrong password!")


# FIRST WINDOW
loginWindow = tk.Tk()
loginWindow.title("Login")
loginWindow.geometry("800x600")
loginWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets 2x as big.
loginWindow.configure(background=bg1)  # Changes background color

loginPassword = tk.Entry(loginWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
loginButton = tk.Button(loginWindow, text="Login", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=login)
wrongPassword = tk.Label(loginWindow, text="", fg=fg1, bg=bg1)  # placeholder for wrong password label

loginPassword.pack(pady=10)
loginButton.pack(pady=10)
wrongPassword.pack(pady=10)

loginWindow.mainloop()
