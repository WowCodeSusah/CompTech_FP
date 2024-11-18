from tkinter import *

current_x, current_y = 0,0
color = 'black'

def new_canvas():
    canvas.delete('all')
    
window = Tk()

inputtxt = Text(window, height = 5, width = 20) 
inputtxt.pack() 

window.title('Paint')
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)

canvas= Canvas(window,background='white') 
canvas.grid(row=0,column=0,sticky='nsew')

window.mainloop()
