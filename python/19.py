import pathlib
import regex as re

path = pathlib.Path(".").parent / "inputs/19.txt"
with open(path, "r") as f:
    rules_lines, tickets = f.read().split("\n\n")

rules_lines = rules_lines.splitlines()
rules_dict = {}
for line in rules_lines:
    n, rule = line.split(": ")
    rule = rule.split(" | ")
    # n = int(n)
    rules_dict[n] = rule


def transform_rule(n, rules_dict):
    flag = False
    if rules_dict[n][0] == '"a"':  # pr '""'
        return "a"
    elif rules_dict[n][0] == '"b"':
        return "b"
    else:
        ## cheating!
        if n == "11":
            forty_two = transform_rule("42", rules_dict)
            thirty_one = transform_rule("31", rules_dict)
            strr = (
                "(?P<r>"
                + forty_two
                + "(?P&r)?"
                + thirty_one
                + ")"
            )
            return strr

        strr = "("
        for index, i in enumerate(rules_dict[n]):
            rule = i.split(" ")
            if index > 0:
                strr += "|"
            for j in rule:
                if j == n:
                    strr += "TO_REPLACE"
                else:
                    strr += transform_rule(j, rules_dict)
        strr += ")"
        if strr.endswith("TO_REPLACE)"):
            strr = strr.replace("TO_REPLACE", "+")

        return strr


val = "^" + transform_rule("0", rules_dict) + "$"

count = 0
for ticket in tickets.splitlines():
    res = re.match(val, ticket)
    if res:
        count += 1

print(count)
