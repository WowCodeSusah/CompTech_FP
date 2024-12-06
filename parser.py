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

parser = Lark(grammar, start='sentence', ambiguity='explicit')

sentence = 'he eats house'

def make_png(filename):
    tree.pydot__tree_to_png( parser.parse(sentence), filename)

def make_dot(filename):
    tree.pydot__tree_to_dot( parser.parse(sentence), filename)

if __name__ == '__main__':
    print(parser.parse(sentence).pretty())
    make_png('hello.png')
    # make_dot(sys.argv[0])