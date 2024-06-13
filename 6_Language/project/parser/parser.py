import nltk
import sys
from nltk.tokenize import word_tokenize
from nltk.tree import Tree

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | VP
NP -> Det N | Det AdjP N | N | AdjP N | Det N PP | NP PP | NP Conj NP
VP -> V | V NP | V PP | V NP PP | VP Conj VP | VP PP
PP -> P NP
AdjP -> Adj | Adj AdjP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        s = input("Sentence: ")

    s = preprocess(s)

    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))

def preprocess(sentence):
    words = word_tokenize(sentence.lower())
    return [word for word in words if any(c.isalpha() for c in word)]

def np_chunk(tree):
    chunks=[]
    for subtree in tree.subtrees(lambda tree_node: tree_node.label()=="NP"):
        nested_np = 0
        for i in subtree.subtrees(lambda tree_node: tree_node.label()=="NP"):
            nested_np += 1
        if nested_np == 1:
            chunks.append(subtree)
    return chunks
if __name__ == "__main__":
    main()
