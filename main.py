from email import message
import sqlite3
import tkinter as tk
from tkinter import ttk
import sys
import csv

# Defualt theme
bg1 = "#3c3836"
fg1 = "#ebdbb2"
gruvYellow = "#d79921"  # Called gruv yellow as yellow is already a system color


def changed_theme():
    global errorLabel
    errorLabel.configure(text="Theme will change after login.")


def dark_theme():  # Dark theme hexcodes
    global bg1
    global fg1
    global gruvYellow
    # Taken from Gruvbox Dark theme
    bg1 = "#3c3836"
    fg1 = "#ebdbb2"
    gruvYellow = "#d79921"  # Called gruv yellow as yellow is already a system color
    changed_theme()


def light_theme():  # Light theme hexcodes
    global bg1
    global fg1
    global gruvYellow
    # Taken from Gruvbox Light theme
    bg1 = "#ebdbb2"
    fg1 = "#3c3836"
    gruvYellow = "#d79921"  # Called gruv yellow as yellow is already a system color
    changed_theme()


def create_product_table_UI():  # (Re)Creates the product table
    def back():
        global window
        createWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def proceed():
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
        back()
        messageLabel.configure(text="Table created!")

    global window
    window.destroy()
    createWindow = tk.Tk()
    createWindow.title("(Re)Create Product Table")
    createWindow.geometry("800x600")
    createWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    createWindow.configure(background=bg1)

   # Tkinter widgets
    confirmLabel = tk.Label(createWindow, text="This action will overwrite any prexisting database with the same name,\nare you sure you would like to continue?", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0")
    proceedButton = tk.Button(createWindow, text="Proceed", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=proceed)
    backButton = tk.Button(createWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=back)

    confirmLabel.pack(anchor="n",  pady=10)
    proceedButton.pack(pady=10)
    backButton.pack(pady=10)


def insert_UI():  # Inserts a new product into the database
    def back():
        global window
        insertWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def insert_data(values):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "insert into Product (Name, Price) values (?,?)"
            cursor.execute(sql, values)
            db.commit()

    def confirm():
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
            back()
            messageLabel.configure(text="Item added!")

    global window
    window.destroy()
    insertWindow = tk.Tk()
    insertWindow.title("Add to Product Table")
    insertWindow.geometry("800x600")
    insertWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    insertWindow.configure(background=bg1)
    insertWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

   # Tkinter widgets
    errorLabel = tk.Label(insertWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    productPromptLabel = tk.Label(insertWindow, text="Product Name:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    costPromptLabel = tk.Label(insertWindow, text="Cost:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    productEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    costEntry = tk.Entry(insertWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    confirmButton = tk.Button(insertWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=confirm)
    backButton = tk.Button(insertWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=back)

    errorLabel.grid(row=0, column=0, padx=10, pady=10)

    productPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    productPromptLabel.grid_columnconfigure(1, weight=1)
    costPromptLabel.grid(row=2, column=0, padx=10, pady=10)
    costPromptLabel.grid_columnconfigure(1, weight=1)
    productEntry.grid(row=1, column=1, padx=10, pady=10)
    productEntry.grid_columnconfigure(1, weight=1)
    costEntry.grid(row=2, column=1, padx=10, pady=10)
    costEntry.grid_columnconfigure(1, weight=1)
    confirmButton.grid(row=3, column=0, padx=10, pady=10)
    confirmButton.grid_columnconfigure(1, weight=1)
    backButton.grid(row=3, column=1, padx=10, pady=10)
    backButton.grid_columnconfigure(1, weight=1)


def update_UI():  # Updates a product in the database
    def back():
        global window
        updateWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def update_product(data):
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = "update Product set Name=?, Price=? where ProductID=?"
            cursor.execute(sql, data)
            db.commit()

    def confirm():
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
            back()
            messageLabel.configure(text="Item updated!")

    global window
    window.destroy()
    updateWindow = tk.Tk()
    updateWindow.title("Update Product Table")
    updateWindow.geometry("800x600")
    updateWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    updateWindow.configure(background=bg1)
    updateWindow.grid_columnconfigure(0, weight=1)  # Makes the column stretch to fill the window.

   # Tkinter widgets
    errorLabel = tk.Label(updateWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(updateWindow, text="Product ID:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    productPromptLabel = tk.Label(updateWindow, text="New Product Name:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    costPromptLabel = tk.Label(updateWindow, text="New Cost:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    productEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    costEntry = tk.Entry(updateWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    confirmButton = tk.Button(updateWindow, text="Confirm", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=confirm)
    backButton = tk.Button(updateWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=back)

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
    confirmButton.grid(row=4, column=0, padx=10, pady=10)
    confirmButton.grid_columnconfigure(1, weight=1)
    backButton.grid(row=4, column=1, padx=10, pady=10)
    backButton.grid_columnconfigure(1, weight=1)


def delete_UI():  # Deletes a product from the database
    def cancel():  # Close window
        global window
        deleteWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def delete_product(data):  # Delete product
        global method
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            sql = f"delete from product where {method}=?"
            cursor.execute(sql, (data,))  # Data is formmat as a tuple. This took way too long to figure out.
            db.commit()

    def confirm_productID():  # Select product id to delete
        inpID = idEntry.get()  # Get text field contents
        if inpID == "":
            errorLabel.configure(text="Please fill the ID input!")
        else:
            global productsAll
            global method
            method = "ProductID"
            product_ID = inpID
            data = (product_ID)
            delete_product(data)
            cancel()
            messageLabel.configure(text="Item deleted!")

    def confirm_product_name():  # Select product name to delete
        inpID = idEntry.get()  # Get text field contents
        if inpID == "":
            errorLabel.configure(text="Please fill the ID input!")
        else:
            global productsAll
            global method
            method = "Name"
            product_Name = inpID
            data = (product_Name)
            delete_product(data)
            cancel()
            messageLabel.configure(text="Item deleted!")

    global window
    window.destroy()
    deleteWindow = tk.Tk()
    deleteWindow.title("Delete items from the Product Table")
    deleteWindow.geometry("800x600")
    deleteWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    deleteWindow.configure(background=bg1)

    # TKinter widgets
    errorLabel = tk.Label(deleteWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(deleteWindow, text="Input Product ID or name:\nBe sure to select the correct option.", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(deleteWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    confirmProductIDButton = tk.Button(deleteWindow, text="Delete ProductID", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=confirm_productID)
    confirmProductNameButton = tk.Button(deleteWindow, text="Delete Name", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=confirm_product_name)
    cancelButton = tk.Button(deleteWindow, text="Cancel", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=cancel)

    errorLabel.pack(anchor="n", pady=10)
    idPromptLabel.pack(pady=10)
    idEntry.pack(pady=10)
    confirmProductIDButton.pack(pady=10)
    confirmProductNameButton.pack(pady=10)
    cancelButton.pack(pady=10)


def find_products_UI():  # Find products in the database
    def back():  # Close window
        global window
        findWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def select_product(id):  # Get product info
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute("select Name,Price from Product where ProductID=?", (id,))
            product = cursor.fetchone()
            return product

    def search():  # Display product info
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

   # Tkinter widgets
    errorLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # placeholder for error message
    idPromptLabel = tk.Label(findWindow, text="Product ID:", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    idEntry = tk.Entry(findWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
    searchButton = tk.Button(findWindow, text="Search", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=search)
    backButton = tk.Button(findWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=back)
    nameLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # part of answer
    costLabel = tk.Label(findWindow, text="", fg=fg1, bg=bg1)  # part of answer

    errorLabel.grid(row=0, column=0, padx=10, pady=10)

    idPromptLabel.grid(row=1, column=0, padx=10, pady=10)
    idPromptLabel.grid_columnconfigure(1, weight=1)
    idEntry.grid(row=1, column=1, padx=10, pady=10)
    idEntry.grid_columnconfigure(1, weight=1)
    searchButton.grid(row=4, column=0, padx=10, pady=10)
    searchButton.grid_columnconfigure(1, weight=1)
    backButton.grid(row=4, column=1, padx=10, pady=10)
    backButton.grid_columnconfigure(1, weight=1)
    nameLabel.grid(row=5, column=0, padx=10, pady=10)
    nameLabel.grid_columnconfigure(1, weight=1)
    costLabel.grid(row=5, column=1, padx=10, pady=10)
    costLabel.grid_columnconfigure(1, weight=1)


def list_products_UI():  # List all products in the database
    def back():  # Close window
        global window
        listWindow.destroy()
        window = tk.Tk()
        window.title("Coffee Shop Database")
        window.geometry("800x600")
        window.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
        window.configure(background=bg1)
        main_menu()

    def sort():  # Sort by given variables
        global direction
        global catagory
        with sqlite3.connect("coffee_shop.db") as db:
            cursor = db.cursor()
            cursor.execute(f"select * from Product order by {catagory} {direction}")
            products = cursor.fetchall()
            productList.delete(0, tk.END)
            for product in products:
                productList.insert(tk.END, product)

    def asc():  # Set the direction to ascending
        global direction
        direction = "ASC"

    def desc():  # Set the direction to desc
        global direction
        direction = "DESC"

    def name():  # Set the catagory to name
        global catagory
        catagory = "Name"

    def price():  # Set the catagory to price
        global catagory
        catagory = "Price"

    global window
    window.destroy()
    listWindow = tk.Tk()
    listWindow.title("List all products")
    listWindow.geometry("800x600")
    listWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
    listWindow.configure(background=bg1)

   # Tkinter widgets
    helpLabel = tk.Label(listWindow, text="Don't see all your data?\nTry scrolling!", fg=gruvYellow, bg=bg1)  # placeholder for error message
    productList = tk.Listbox(listWindow, fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")
    sortNameAscButton = tk.Button(listWindow, text="Sort Name Ascending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0",  command=lambda: (asc(), name(), sort()))
    sortNameDescButton = tk.Button(listWindow, text="Sort Name Descending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=lambda: (desc(), name(), sort()))
    sortPriceAscButton = tk.Button(listWindow, text="Sort Cost Ascending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=lambda: (asc(), price(), sort()))
    sortPriceDescButton = tk.Button(listWindow, text="Sort Cost Descending", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=lambda: (desc(), price(), sort()))
    backButton = tk.Button(listWindow, text="Back", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=back)

    helpLabel.pack(anchor="n", pady=10)
    productList.pack(pady=10)
    sortNameAscButton.pack(pady=10)
    sortNameDescButton.pack(pady=10)
    sortPriceAscButton.pack(pady=10)
    sortPriceDescButton.pack(pady=10)
    backButton.pack(pady=10)

    # Display the list of products
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        productList.delete(0, tk.END)
        for product in products:
            productList.insert(tk.END, product)


def backup_database_UI():  # Backup database. Thanks for the help Prem.
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        with open("coffee_shop.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)
    messageLabel.configure(text="Backed up to CSV!")


def main_menu():  # Main menu
    global messageLabel
    messageLabel = tk.Label(window, text="", fg=fg1, bg=bg1, highlightthickness="0", borderwidth="0")  # Used by submenus to display messages
    createButton = tk.Button(window, text="(Re)Create Product Table", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=create_product_table_UI)
    addButton = tk.Button(window, text="Add new product", fg=fg1, bg=gruvYellow,  highlightthickness="0", borderwidth="0", command=insert_UI)
    updateButton = tk.Button(window, text="Update existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=update_UI)
    deleteButton = tk.Button(window, text="Delete existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=delete_UI)
    findButton = tk.Button(window, text="Find product", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=find_products_UI)
    listButton = tk.Button(window, text="List all products", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=list_products_UI)
    backupButton = tk.Button(window, text="Backup database", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=backup_database_UI)
    exitButton = tk.Button(window, text="Exit", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=sys.exit)

    messageLabel.pack(anchor="n", pady=10)
    createButton.pack(pady=10)
    addButton.pack(pady=10)
    updateButton.pack(pady=10)
    deleteButton.pack(pady=10)
    findButton.pack(pady=10)
    listButton.pack(pady=10)
    backupButton.pack(pady=10)
    exitButton.pack(pady=10)


def login():  # Login to the program
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
        errorLabel.configure(text="Wrong password!")


# FIRST WINDOW
loginWindow = tk.Tk()
loginWindow.title("Login")
loginWindow.geometry("800x600")
loginWindow.tk.call('tk', 'scaling', 0.75)  # Makes all widgets bigger.
loginWindow.configure(background=bg1)  # Changes background color

errorLabel = tk.Label(loginWindow, text="", fg=fg1, bg=bg1)  # placeholder for wrong password label
loginPassword = tk.Entry(loginWindow, fg=bg1, bg=fg1, highlightthickness="0", borderwidth="0")
loginButton = tk.Button(loginWindow, text="Login", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=login)
darkThemeButton = tk.Button(loginWindow, text="Dark Theme", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=dark_theme)
lightThemeButton = tk.Button(loginWindow, text="Light Theme", fg=fg1, bg=gruvYellow, highlightthickness="0", borderwidth="0", command=light_theme)


errorLabel.pack(pady=10)
loginPassword.pack(pady=10)
loginButton.pack(pady=10)
darkThemeButton.pack(pady=10)
lightThemeButton.pack(pady=10)

loginWindow.mainloop()
