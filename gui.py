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


def main_menu():
    window = tk.Tk()
    window.title("Davis\' Coffee Shop Database")
    window.geometry("800x600")
    window.tk.call('tk', 'scaling', 2.0)  # Makes all widgets 2x as big.

    window.configure(background=bg1)  # changes background color

    # Product table menu
    createButton = tk.Button(text="(Re)Create Product Table", fg=fg1, bg=gruvYellow, highlightthickness="0", command=backend.create_product_table_UI).pack(anchor='n')
    addButton = tk.Button(text="Add new product", fg=fg1, bg=gruvYellow,  highlightthickness="0", command=backend.insert_UI).pack()
    updateButton = tk.Button(text="Update existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", command=backend.update_UI).pack()
    deleteButton = tk.Button(text="Delete existing product", fg=fg1, bg=gruvYellow, highlightthickness="0", command=backend.delete_UI).pack()
    findButton = tk.Button(text="Find products", fg=fg1, bg=gruvYellow, highlightthickness="0", command=backend.select_products_UI).pack()
    listButton = tk.Button(text="List products", fg=fg1, bg=gruvYellow, highlightthickness="0", command=backend.list_products_UI).pack()
    exitButton = tk.Button(text="Exit", fg=fg1, bg=gruvYellow, highlightthickness="0", command=sys.exit).pack()

    window.mainloop()
