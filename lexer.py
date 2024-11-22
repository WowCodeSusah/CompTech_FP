# Token List
tokens = ('Adjective', 'Verb', 'Adverb', 'Noun', 'Subject')

def openFile(file):
    f = open(file, 'r')
    FileList = f.read()
    FileList = FileList.split(',')
    return FileList 

# List of all Words
ListOfNoun = openFile('TextFiles/Noun.txt')
ListOfAdjective = openFile('TextFiles/Adjective.txt')
ListOfVerb = openFile('TextFiles/Adjective.txt')
ListofAdverb = openFile('TextFiles/Adverb.txt')
ListofSubject = openFile('TextFiles/Subject.txt')

# All the functions
def t_Noun(t):
    if t in ListOfNoun:
        return True
    else:
        return False

def t_Verb(t):
    if t in ListOfVerb:
        return True
    else:
        return False

def t_Adverb(t):
    if t in ListofAdverb:
        return True
    else:
        return False

def t_Adjective(t):
    if t in ListOfAdjective:
        return True
    else:
        return False    

def t_Subject(t):
    if t in ListofSubject:
        return True
    else:
        return False

# Test it out
test = "big person said mostly"

# Lexer Algorithm
def LexerAlgorithm(Input):
    Lexer = []
    rawData = Input.split(' ')
    for data in rawData:
        if t_Adjective(data):
            Lexer.append(['Adjective', data])
        elif t_Adverb(data):
            Lexer.append(['Adverb', data])
        elif t_Noun(data):
            Lexer.append(['Noun', data])
        elif t_Subject(data):
            Lexer.append(['Subject', data])
        elif t_Verb(data):
            Lexer.append(['Verb', data])
        else:
            return print('Lexer Error')
    return Lexer

print(LexerAlgorithm(test))

        
    


