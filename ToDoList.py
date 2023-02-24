import tkinter as tk

# setInitialPosition -> Defines the initial position for an app passed as parameter
def setInitialPosition(appToSetToCenter):
    # Set coordinates
    xAxis = appToSetToCenter.winfo_screenwidth() // 2
    yAxis = int(appToSetToCenter.winfo_screenheight() * 0.1)
    
    # Set app position
    appToSetToCenter.geometry('500x600+' + str(xAxis) + '+' + str(yAxis))

# Init app
root = tk.Tk()

# App settings
root.title("Bardo app")
#root.eval("tk::PlaceWindow . center")
setInitialPosition(appToSetToCenter = root)

# Initial app structure settings
initialFrame = tk.Frame(root, width=500, height=600, bg="#EC00FF")
initialFrame.grid(row=0, column=0)

# Run app
root.mainloop()