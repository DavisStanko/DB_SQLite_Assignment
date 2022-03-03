import tkinter as tk

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
prompt = tk.Label(foreground=fg1, background=bg1, text="")

# Place the widgets
prompt.pack(anchor="n")  # Anchor north (top middle)

window.mainloop()
