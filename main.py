import tkinter as tk
from tkinter import PhotoImage
from lark import Lark, tree

grammar = """
    sentence: NOUN pred obj comp   
    
    pred: VERB | 
    obj: OBJ | ADJ OBJ |
    comp: ADJ | ADV | 

    NOUN: "he" | "she" | "it"
    OBJ: "house" | "ball"
    ADV: "happily"
    VERB: "eats" | "sits" | "plays"
    ADJ: "red"

    %import common.WS
    %ignore WS
"""

def parser(sentence, pngName ,grammar = grammar):
    parser = Lark(grammar, start='sentence', ambiguity='explicit')

    def make_png(filename):
        tree.pydot__tree_to_png( parser.parse(sentence), filename)

    def make_dot(filename):
        tree.pydot__tree_to_dot( parser.parse(sentence), filename)

    if __name__ == '__main__':
        print(parser.parse(sentence).pretty())
        make_png(pngName + '.png')
        # make_dot(sys.argv[0])
    
    return pngName + '.png'


# Create main frame
frame = tk.Tk()
frame.title("English to Semaphore")
frame.geometry('1000x700+0+0')

parsed = False
parseTreeName = ''

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    global parsed
    global count
    global parseTreeName

    if parsed == False:
        parseTreeName = parser(inp, 'testName')
        parsed = True
    else:
        pass

    parseTreeImage = tk.PhotoImage(file=parseTreeName)
    parseTree_label.config(image=parseTreeImage)
    parseTree_label.image = parseTreeImage
    
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

        count = count + 1
        frame.after(1000, printInput)
    else:
        count = 0
        parsed = False
    

# Create a container frame for top-left content
top_left_frame = tk.Frame(frame)
top_left_frame.pack()  # Center vertically

# Text input
inputtxt = tk.Text(top_left_frame, height=5, width=50)
inputtxt.pack()

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

parseTree_label = tk.Label(top_left_frame, image='')
parseTree_label.pack(pady=5)

frame.mainloop()