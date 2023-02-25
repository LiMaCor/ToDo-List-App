import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox

# Define variable for app background color
appBackgroundColor = "#EC00FF"

# setInitialPosition -> Defines the initial position for an app passed as parameter
def setInitialPosition(appToSetToCenter):
    # Set coordinates
    xAxis = appToSetToCenter.winfo_screenwidth() // 2
    yAxis = int(appToSetToCenter.winfo_screenheight() * 0.1)
    
    # Set app position
    appToSetToCenter.geometry('500x600+' + str(xAxis) + '+' + str(yAxis))

# printModalMessage -> Shows a modal window to the user with a static message
def printModalMessage():
    infoMessageModal = messagebox.showinfo(
        title="Info modal message",
        message="A bard throws an apple to a guard and everything explodes"
    )

# setAppFrameLogo -> Defines base logo for the app
def setAppFrameLogo(appFrameToSetLogo):
    appFrameLogo = ImageTk.PhotoImage(file="assets\logo-bard.png")
    appFrameLogoWidget = tk.Label(
        appFrameToSetLogo, 
        image=appFrameLogo, 
        bg=appBackgroundColor
    )
    
    appFrameLogoWidget.image = appFrameLogo
    appFrameLogoWidget.pack()

# setAppFrameSlogan -> Defines a static base slogan for the app
def setAppFrameSlogan(appFrameToSetSlogan):
    appFrameSlogan = tk.Label(
        appFrameToSetSlogan,
        text="Bard's inspiration intensifies!",
        bg=appBackgroundColor,
        fg="white",
        font=("TkMenuFont", 14)
    )

    appFrameSlogan.pack()

# setAppFrameButton -> Defines a button which shows a modal message on click
def setAppFrameButton(appFrameToSetButton):
    appFrameButton = tk.Button(
        appFrameToSetButton,
        text="Request",
        font=("TkHeadingFont", 20),
        bg="#900C3F",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:printModalMessage()
    )
    
    appFrameButton.pack()

# setAppFrame -> Defines basic structure for the app
def setAppFrame(appToInitStructure):
    appFrame = tk.Frame(appToInitStructure, width=500, height=600, bg=appBackgroundColor)
    appFrame.grid(row=0, column=0)
    appFrame.pack_propagate(False)
    
    setAppFrameLogo(appFrame)
    setAppFrameSlogan(appFrame)
    setAppFrameButton(appFrame)

# Init app
root = tk.Tk()

# App settings
root.title("Bardo app")
setInitialPosition(appToSetToCenter = root)
setAppFrame(appToInitStructure = root)

# Run app
root.mainloop()