# Token List
tokens = ('Adjective', 'Verb', 'Adverb', 'Noun', 'Subject', 'Preposition', 'Determiner')

def openFile(file):
    f = open(file, 'r')
    FileList = f.read()
    FileList = FileList.replace('\n', '')
    FileList = FileList.split(',')
    return FileList 

# List of all Words
ListOfNoun = openFile('TextFiles/Noun.txt')
ListOfAdjective = openFile('TextFiles/Adjective.txt')
ListOfVerb = openFile('TextFiles/Verb.txt')
ListofAdverb = openFile('TextFiles/Adverb.txt')
ListofSubject = openFile('TextFiles/Subject.txt')
ListofPreposition = openFile('TextFiles/Preposition.txt')
ListodDeterminer = openFile('TextFiles/Determiner.txt')

# All the functions
def t_Noun(t):
    if t in ListOfNoun:
        return True
    else:
        return False

def t_Verb(t):
    if t in ListOfVerb or t[:-1] in ListOfVerb:
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
    
def t_Preposition(t):
    if t in ListofPreposition:
        return True
    else:
        return False
    
def t_Determiner(t):
    if t in ListodDeterminer:
        return True
    else:
        return False

# Test it out
test = "he calmly sits chair"

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
        elif t_Preposition(data):
            Lexer.append(['Preposition', data])
        elif t_Determiner(data):
            Lexer.append(['Determiner', data])
        else:
            return print('Lexer Error')
    return Lexer

print(LexerAlgorithm(test))

        
    


