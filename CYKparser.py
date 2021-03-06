import os.path
import cfgtocnf

class Node:

    def __init__(self, symbol, anak1, anak2=None):
        self.symbol = symbol
        self.anak1 = anak1
        self.anak2 = anak2

    def __repr__(self):
        return self.symbol


class Parser:
    def __init__(self, grammar, sentence):
        self.parsetabel = None
        self.prods = {}
        self.grammar = None
        self.string_input = None
        self.sentence = sentence
        if os.path.isfile(grammar):
            self.grammar_from_file(grammar)
        else:
            self.grammar_from_string(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):
        if os.path.isfile(sentence):
            with open(sentence) as inp:
                self.string_input = inp.readline().split()
                if parse:
                    self.parse()
        else:
            self.string_input = sentence.split()
            self.sentence = sentence
    def __del__(self):
        print("Terminating parser...")
    def grammar_from_file(self, grammar):
        self.grammar = cfgtocnf.convert_grammar(cfgtocnf.read_grammar(grammar))

    def grammar_from_string(self, grammar):
        self.grammar = cfgtocnf.convert_grammar([x.replace("->", "").split() for x in grammar.split("\n")])

    def parse(self):
        string_length = len(self.string_input)
        self.parsetabel = [[[] for x in range(string_length - y)] for y in range(string_length)]

        for i, kata in enumerate(self.string_input):
            for rule in self.grammar:
                if f"'{kata}'" == rule[1]:
                    self.parsetabel[0][i].append(Node(rule[0], kata))
        for wordoption in range(2, string_length + 1):
            for cellpertama in range(0, string_length - wordoption + 1):
                for ukkiri in range(1, wordoption):
                    ukkanan = wordoption - ukkiri
                    kotakkiri = self.parsetabel[ukkiri - 1][cellpertama]
                    kotakkanan = self.parsetabel[ukkanan - 1][cellpertama + ukkiri]
                    for rule in self.grammar:
                        ndkiri = [n for n in kotakkiri if n.symbol == rule[1]]
                        if ndkiri:
                            ndkanan = [n for n in kotakkanan if n.symbol == rule[2]]
                            self.parsetabel[wordoption - 1][cellpertama].extend([Node(rule[0], kri, knan) for kri in ndkiri for knan in ndkanan])
    def print_tree(self, output=True):
        startsymbol = self.grammar[0][0]
        ndakhir = [n for n in self.parsetabel[-1][0] if n.symbol == startsymbol]
        if ndakhir:
            if output:
                return True
        else:
            
            print("Kalimat tidak termuat dalam bahasa dari grammar yang diberikan!")
            print(self.sentence)
            return False
            