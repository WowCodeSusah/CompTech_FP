import tkinter as tk 
from tkinter import PhotoImage
  
frame = tk.Tk() 
frame.title("English to Semaphore") 
frame.geometry('1000x500') 

def printInput():
    global count
    inp = inputtxt.get(1.0, "end-1c") 
    stringList = list(inp)
    if len(stringList) > count:
        lbl.config(text = "Provided Input: "+ stringList[count])
        flagtext = stringList[count].upper()
        if flagtext == " ":
            image.config(file= "Resouces/Ready.png")
        else:
            image.config(file= "Resouces/"+ flagtext +".png")

        frame.after(1000, printInput)
        count = count + 1
    else:
        count = 0

inputtxt = tk.Text(frame, height = 10, width = 50) 
inputtxt.pack()

count = 0
  
# Load the image 
image = PhotoImage(file="Resouces/Ready.png")

# Create a label to display the image
image_label = tk.Label(frame, image=image)
image_label.pack(pady=10)

# Button Creation 
printButton = tk.Button(frame, text = "Translate", command= printInput, width=30, height=2) 
printButton.pack(pady= 10) 

# Label Creation 
lbl = tk.Label(frame, text = "") 
lbl.pack() 
frame.mainloop() 