import pathlib
import pyparsing as pp

path = pathlib.Path(".").parent / "inputs/18.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

# parsing is a shameless plug from stackoverflow with some modification

integer = pp.Word(pp.nums)
LPAR, RPAR = map(pp.Suppress, "()")
expr = pp.Forward()
operand = integer
factor = operand | pp.Group(LPAR + expr + RPAR)
term = factor + pp.ZeroOrMore(pp.oneOf("* /") + factor)
expr <<= term + pp.ZeroOrMore(pp.oneOf("+ -") + term)

expr = pp.infixNotation(
    operand,
    [
        # modification is here
        # p1
        #
        # (pp.oneOf("+ *"), 2, pp.opAssoc.LEFT),

        (pp.oneOf("+"), 2, pp.opAssoc.LEFT),
        (pp.oneOf("*"), 2, pp.opAssoc.LEFT),
    ],
)


def calculate(first, op, second):
    if op == "+":
        return int(first) + int(second)
    else:
        return int(first) * int(second)


def evaluate(expr):
    if isinstance(expr, str):
        return int(expr)
    else:
        if len(expr) == 1:
            expr = expr[0]
            if isinstance(expr, str):
                return int(expr)
        first = evaluate(expr[0])
        op = expr[1]
        val = calculate(first, op, evaluate(expr[2:]))
        return val

sum = 0
for line in lines:
    expression = expr.parseString(line[::-1].replace(")", ":").replace("(", ")").replace(":", "("))
    sum += evaluate(expression.asList())
print(sum)
