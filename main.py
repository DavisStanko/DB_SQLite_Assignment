import sqlite3
import tkinter as tk
from tkinter import ttk
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
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def yes():
        global messageLabel
        db_name = "coffee_shop.db"
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
    createWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    createWindow.configure(background=bg1)
    createWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    confirmLabel = tk.Label(createWindow, text="This action will overwrite any prexisting database with the same name,\nare you sure you would like to continue?", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0",)
    yesButton = tk.Button(createWindow, text="Proceed", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(createWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

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
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def insert_data(values):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "insert into Product (Name, Price) values (?,?)"
            cursor.execute(sql, values)
            db.commit()

    def yes():
        inpProduct = productEntry.get()  # Get text field contents
        inpCost = costEntry.get()  # Get text field contents
        if inpProduct == "" or inpCost == "":
            errorLabel.configure(text="Please fill in both inputs!")
        else:
            global productsAll
            product_name = inpProduct
            product_price = inpCost
            product = (product_name, product_price)
            insert_data(product)
            no()
            messageLabel.configure(text="Item added!")

    global window
    window.destroy()
    insertWindow = tk.Tk()
    insertWindow.title("Add to Product Table")
    insertWindow.geometry("800x600")
    insertWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    insertWindow.configure(background=bg1)
    insertWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(insertWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    productPromptLabel = tk.Label(insertWindow, text="Product Name:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    costPromptLabel = tk.Label(insertWindow, text="Cost:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    productEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    costEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    yesButton = tk.Button(insertWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(insertWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

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


def update_UI():
    def no():
        global window
        updateWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def update_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "update Product set Name=?, Price=? where ProductID=?"
            cursor.execute(sql, data)
            db.commit()

    def yes():
        inpID = idEntry.get()  # Get text field contents
        inpProduct = productEntry.get()  # Get text field contents
        inpCost = costEntry.get()  # Get text field contents
        if inpID == "" or inpProduct == "" or inpCost == "":
            errorLabel.configure(text="Please fill in all inputs!")
        else:
            global productsAll
            product_ID = inpID
            product_name = inpProduct
            product_price = inpCost
            data = (product_name, product_price, product_ID)
            update_product(data)
            no()
            messageLabel.configure(text="Item updated!")

    global window
    window.destroy()
    updateWindow = tk.Tk()
    updateWindow.title("Update Product Table")
    updateWindow.geometry("800x600")
    updateWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    updateWindow.configure(background=bg1)
    updateWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(updateWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(updateWindow, text="Product ID:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    productPromptLabel = tk.Label(updateWindow, text="New Product Name:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    costPromptLabel = tk.Label(updateWindow, text="New Cost:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    productEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    costEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    yesButton = tk.Button(updateWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(updateWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

    errorLabel.grid(row=0, column=0, padx=10, pady=10)

    idPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    idPromptLabel.grid_columnconfigure(1, weight=1)
    productPromptLabel.grid(row=2, column=0, padx=10, pady=10)
    productPromptLabel.grid_columnconfigure(1, weight=1)
    costPromptLabel.grid(row=3, column=0, padx=10, pady=10)
    costPromptLabel.grid_columnconfigure(1, weight=1)
    idEntry.grid(row=1, column=1, padx=10, pady=10)
    idEntry.grid_columnconfigure(1, weight=1)
    productEntry.grid(row=2, column=1, padx=10, pady=10)
    productEntry.grid_columnconfigure(1, weight=1)
    costEntry.grid(row=3, column=1, padx=10, pady=10)
    costEntry.grid_columnconfigure(1, weight=1)
    yesButton.grid(row=4, column=0, padx=10, pady=10)
    yesButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=4, column=1, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)


def delete_UI():
    def no():
        global window
        deleteWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def delete_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "delete from product where ProductID=?"
            cursor.execute(sql, data)
            db.commit()

    def yes():
        inpID = idEntry.get()  # Get text field contents
        if inpID == "":
            errorLabel.configure(text="Please fill the ID input!")
        else:
            global productsAll
            product_ID = inpID
            data = (product_ID,)
            delete_product(data)
            no()
            messageLabel.configure(text="Item deleted!")

    global window
    window.destroy()
    deleteWindow = tk.Tk()
    deleteWindow.title("Delete items from the Product Table")
    deleteWindow.geometry("800x600")
    deleteWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    deleteWindow.configure(background=bg1)
    deleteWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(deleteWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(deleteWindow, text="Product ID:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(deleteWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    yesButton = tk.Button(deleteWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(deleteWindow, text="Cancel", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)

    errorLabel.grid(row=0, column=0, padx=10, pady=10)

    idPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    idPromptLabel.grid_columnconfigure(1, weight=1)
    idEntry.grid(row=1, column=1, padx=10, pady=10)
    idEntry.grid_columnconfigure(1, weight=1)
    yesButton.grid(row=4, column=0, padx=10, pady=10)
    yesButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=4, column=1, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)


def find_products_UI():
    def no():
        global window
        findWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def select_product(id):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute(
                "select Name,Price from Product where ProductID=?", (id,))
            product = cursor.fetchone()
            return product

    def yes():
        inpID = idEntry.get()  # Get text field contents
        if inpID == "":
            errorLabel.configure(text="Please fill the ID input!")
        else:
            answer = select_product(inpID)
            nameLabel.configure(text=f"Product: {answer[0]}")
            costLabel.configure(text=f"Cost: {str(answer[1])}")

    global window
    window.destroy()
    findWindow = tk.Tk()
    findWindow.title("Delete items from the Product Table")
    findWindow.geometry("800x600")
    findWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    findWindow.configure(background=bg1)
    findWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(findWindow, text="Product ID:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(findWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    yesButton = tk.Button(findWindow, text="Search", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=yes)
    noButton = tk.Button(findWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)
    nameLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # part of answer
    costLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # part of answer

    errorLabel.grid(row=0, column=0, padx=10, pady=10)

    idPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    idPromptLabel.grid_columnconfigure(1, weight=1)
    idEntry.grid(row=1, column=1, padx=10, pady=10)
    idEntry.grid_columnconfigure(1, weight=1)
    yesButton.grid(row=4, column=0, padx=10, pady=10)
    yesButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=4, column=1, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)
    nameLabel.grid(row=5, column=0, padx=10, pady=10)
    nameLabel.grid_columnconfigure(1, weight=1)
    costLabel.grid(row=5, column=1, padx=10, pady=10)
    costLabel.grid_columnconfigure(1, weight=1)


def list_products_UI():
    def no():
        global window
        listWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()

    def sort():
        global direction
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute(f"select * from Product order by Name {direction}")
            products = cursor.fetchall()
            productList.delete(0, tk.END)
            for product in products:
                productList.insert(tk.END, product)

    def asc():
        global direction
        direction = "ASC"
        sort()

    def desc():
        global direction
        direction = "DESC"
        sort()

    def yes():
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from Product")
            products = cursor.fetchall()
            productList.delete(0, tk.END)
            for product in products:
                productList.insert(tk.END, product)

    global window
    window.destroy()
    listWindow = tk.Tk()
    listWindow.title("List all products")
    listWindow.geometry("800x600")
    listWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    listWindow.configure(background=bg1)
    listWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

    # Options
    errorLabel = tk.Label(listWindow, text="Don't see all your data?\nTry scrolling!", fg=gruvYellow, bg=bg1)  # placeholder for error message
    sortNameAscButton = tk.Button(listWindow, text="Sort Name Ascending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=asc)
    sortNameDescButton = tk.Button(listWindow, text="Sort Name Descending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=desc)
    noButton = tk.Button(listWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=no)
    productList = tk.Listbox(listWindow, fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")

    errorLabel.grid(row=0, column=0, padx=10, pady=10)
    errorLabel.grid_columnconfigure(1, weight=1)
    productList.grid(row=1, column=0, padx=10, pady=10)
    productList.grid_columnconfigure(1, weight=1)
    sortNameAscButton.grid(row=2, column=0, padx=10, pady=10)
    sortNameAscButton.grid_columnconfigure(1, weight=1)
    sortNameDescButton.grid(row=3, column=0, padx=10, pady=10)
    sortNameDescButton.grid_columnconfigure(1, weight=1)
    noButton.grid(row=4, column=0, padx=10, pady=10)
    noButton.grid_columnconfigure(1, weight=1)

    yes()


def main_menu():
    global messageLabel
    # Product table menu
    messageLabel = tk.Label(window, text="", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    createButton = tk.Button(window, text="(Re)Create Product Table", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=create_product_table_UI)
    addButton = tk.Button(window, text="Add new product", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=insert_UI)
    updateButton = tk.Button(window, text="Update existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=update_UI)
    deleteButton = tk.Button(window, text="Delete existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=delete_UI)
    findButton = tk.Button(window, text="Find product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=find_products_UI)
    listButton = tk.Button(window, text="List all products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=list_products_UI)
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
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        window.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.
        main_menu()
    else:
        wrongPassword.configure(text="Wrong password!")


# FIRST WINDOW
loginWindow = tk.Tk()
loginWindow.title("Login")
loginWindow.geometry("800x600")
loginWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
loginWindow.configure(background=bg1)  # Changes background color

loginPassword = tk.Entry(loginWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
loginButton = tk.Button(loginWindow, text="Login", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=login)
wrongPassword = tk.Label(loginWindow, text="", fg=fg1, bg=bg1)  # placeholder for wrong password label

loginPassword.pack(pady=10)
loginButton.pack(pady=10)
wrongPassword.pack(pady=10)

loginWindow.mainloop()
