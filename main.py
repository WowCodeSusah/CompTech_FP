import tkinter as tk
from tkinter import PhotoImage

# Create main frame
frame = tk.Tk()
frame.title("English to Semaphore")
frame.geometry('1000x500+0+0')

def printInput():
    global count
    inp = inputtxt.get(1.0, "end-1c")
    stringList = list(inp)
    if len(stringList) > count:
        lbl.config(text="Provided Input: " + stringList[count])
        flagtext = stringList[count].upper()
        if flagtext == " ":
            image_label.config(image=ready_image)  
        else:
            try:
                flag_image = tk.PhotoImage(file="Resouces/" + flagtext + ".png")
                image_label.config(image=flag_image)
                image_label.image = flag_image 
            except Exception as e:
                lbl.config(text=f"Error loading image for '{flagtext}'")

        frame.after(1000, printInput)
        count += 1
    else:
        count = 0

# Create a container frame for top-left content
top_left_frame = tk.Frame(frame)
top_left_frame.pack(anchor="nw", padx=10, pady=10, expand=True) 

# Text input
inputtxt = tk.Text(top_left_frame, height=5, width=50)
inputtxt.pack(pady=5)

count = 0

# Load the "Ready" image as the default
ready_image = PhotoImage(file="Resouces/Ready.png")

# Create a label to display the semaphore flag image
image_label = tk.Label(top_left_frame, image=ready_image)
image_label.image = ready_image
image_label.pack(pady=5)

# Button to start translation
printButton = tk.Button(top_left_frame, text="Translate", command=printInput, width=30, height=2)
printButton.pack(pady=5)

# Label for output text
lbl = tk.Label(top_left_frame, text="")
lbl.pack(pady=5)

frame.mainloop()