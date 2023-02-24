import tkinter as tk

# Init app
root = tk.Tk()

# App settings
root.title("Bardo app")
root.eval("tk::PlaceWindow . center")

# Initial app structure settings
initialFrame = tk.Frame(root, width=500, height=600, bg="#EC00FF")
initialFrame.grid(row=0, column=0)

# Run app
root.mainloop()