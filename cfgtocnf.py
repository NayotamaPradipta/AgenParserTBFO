# Program untuk menkonversikan grammar CFG ke grammar CNF
# Sudah dimodify sesuai dengan program sendiri

# Global dictionary used for storing the rules.
RULE_DICT = {}


def read_grammar(grammar_file):
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
        # angel = [x.replace("->", "").split() for x in lines]
    return [x.replace("->", "").split() for x in lines]

def add_rule(rule):
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])
def convert_grammar(grammar):
    global RULE_DICT
    unit_productions, result = [], []
    res_append = result.append
    index = 0

    for rule in grammar:
        new_rules = []
        # memisahkan grammar yang hanya punya rule di right 2 nonterminal
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            # memasukkan dari grammar yang termasuk terminal
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", item[0]]
                index += 1
            while len(rule) > 3:
                new_rules += [f"{rule[0]}{str(index)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        add_rule(rule)
        res_append(rule)
        if new_rules:
            res_append(new_rules)
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE_DICT:
            for item in RULE_DICT[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    res_append(new_rule)
                else:
                    unit_productions.append(new_rule)
                add_rule(new_rule)
    return result