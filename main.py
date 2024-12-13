import tkinter as tk
from tkinter import PhotoImage
from lark import Lark, tree

def readWords(file_name):
    with open(file_name, 'r') as file:
        file_contents=file.read()
        words = file_contents.split(',')
        words = [word.strip() for word in words]
    return words

noun_list = readWords('TextFiles/Noun.txt')
verb_list = readWords('TextFiles/Verb.txt')
adjective_list = readWords('TextFiles/Adjective.txt')
adverb_list = readWords('TextFiles/Adverb.txt')
subject_list = readWords('TextFiles/Subject.txt')
preposition_list = readWords('TextFiles/Preposition.txt')
determiner_list = readWords('TextFiles/Determiner.txt')

def is_noun(word):
    return word in noun_list

def is_verb(word):
    return word in verb_list

def is_adjective(word):
    return word in adjective_list

def is_adverb(word):
    return word in adverb_list

def is_subject(word):
    return word in subject_list

def is_preposition(word):
    return word in preposition_list

def is_determiner(word):
    return word in determiner_list

def dynamic_grammar(sentence):
    # Dynamically adjust the grammar based on words in the sentence
    def third_person_singular(verb):
        if verb.endswith("y"):
            return verb[:-1] + "ies"
        elif verb.endswith("s") or verb.endswith("x") or verb.endswith("z") or verb.endswith("ch") or verb.endswith("sh"):
            return verb + "es"
        else:
            return verb + "s"

    dynamic_noun = ' | '.join([f'"{word.strip()}"' for word in noun_list])
    dynamic_subject = ' | '.join([f'"{word.strip()}"' for word in subject_list])
    dynamic_verb = ' | '.join([f'"{word.strip()}"' for word in verb_list])
    dynamic_verb2 = ' | '.join([f'"{third_person_singular(word.strip())}"' for word in verb_list])
    dynamic_adjective = ' | '.join([f'"{word.strip()}"' for word in adjective_list])
    dynamic_adverb = ' | '.join([f'"{word.strip()}"' for word in adverb_list])
    dynamic_determiner = ' | '.join([f'"{word.strip()}"' for word in determiner_list])
    dynamic_preposition = ' | '.join([f'"{word.strip()}"' for word in preposition_list])


    dynamic_grammar = f"""
    sentence: subj pred obj? comp?
    subj: DET NOUN | NOUN | SUBJECT
    pred: VERB | ADV VERB 
    obj: OBJ | DET ADJ? OBJ | OBJ "and" OBJ
    comp: ADJ | ADV | PREP NOUN | PREP DET OBJ 

    NOUN: {dynamic_noun}
    OBJ: {dynamic_noun}
    DET: {dynamic_determiner}
    ADV: {dynamic_adverb}
    VERB: {dynamic_verb} | {dynamic_verb2}
    ADJ: {dynamic_adjective}
    PREP: {dynamic_preposition}
    SUBJECT: {dynamic_subject}

    %import common.WS
    %ignore WS
    """
    return dynamic_grammar



def parser(sentence, pngName ,grammar = None):

    grammar = dynamic_grammar(sentence)

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

    if not parsed:
        parseTreeName = parser(inp, 'testName')
        parsed = True

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

        count += 1
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