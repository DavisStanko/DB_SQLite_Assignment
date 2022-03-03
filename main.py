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


window = tk.Tk()
window.title("Davis\' Coffee Shop Database")
window.geometry("800x600")
window.tk.call('tk', 'scaling', 2.0)  # Makes all widgets 2x as big.

window.configure(background=bg1)  # changes background color

# Create the widgets
# Product table menu
createButton = tk.Button(text="(Re)Create Product Table", fg=fg1, bg=gruvYellow,
                         highlightthickness="0", command=backend.create_product_table_UI)
addButton = tk.Button(text="Add new product", fg=fg1, bg=gruvYellow,
                      highlightthickness="0", command=backend.insert_UI)
updateButton = tk.Button(text="Update existing product", fg=fg1,
                         bg=gruvYellow, highlightthickness="0", command=backend.update_UI)
deleteButton = tk.Button(text="Delete existing product", fg=fg1,
                         bg=gruvYellow, highlightthickness="0", command=backend.delete_UI)
findButton = tk.Button(text="Find products", fg=fg1, bg=gruvYellow,
                       highlightthickness="0", command=backend.select_products_UI)
listButton = tk.Button(text="List products", fg=fg1, bg=gruvYellow,
                       highlightthickness="0", command=backend.list_products_UI)
exitButton = tk.Button(text="Exit", fg=fg1, bg=gruvYellow,
                       highlightthickness="0", command=sys.exit)

# Place the widgets
prompt.pack(anchor="n")  # Anchor north (top middle)
createButton.pack()
addButton.pack()
updateButton.pack()
deleteButton.pack()
findButton.pack()
listButton.pack()
exitButton.pack()

window.mainloop()
