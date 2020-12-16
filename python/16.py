import pathlib


def make_range(rangee):
    ranges_set = set()
    for i in rangee:
        start, end = i.split("-")
        start, end = int(start), int(end) + 1
        ranges_set |= set(range(start, end))
    return ranges_set


path = pathlib.Path(".").parent / "inputs/16.txt"
with open(path, "r") as f:
    rules, my_ticket, nearby_tickets = f.read().split("\n\n")

my_ticket: str = my_ticket.splitlines()[1]
nearby_tickets: str = nearby_tickets.splitlines()[1:]

# uglyyyy, but rules_dict now is {key: rule, value: list of valid numbers}
rules_dict = {
    x.split(": ")[0]: make_range(x.split(": ")[1].split(" or "))
    for x in rules.splitlines()
}

# set for p1
ranges_set: set = set()

for ran in rules_dict.values():
    ranges_set |= ran

list_of_invalid_numbers = []
list_of_valid_tickets = []
for i in nearby_tickets:
    numbers_in_ticket: set = {int(x) for x in i.split(",")}
    if not numbers_in_ticket.issubset(ranges_set):
        diff = numbers_in_ticket - ranges_set
        list_of_invalid_numbers.extend(diff)
    else:
        list_of_valid_tickets.append(i)

summ = sum(list_of_invalid_numbers)
print(summ)


# p2
legend = {x: list(rules_dict.keys()) for x in range(len(nearby_tickets[0].split(",")))}


def remove_unmatches(index, n, rules_dict: dict, legend: dict):
    # if number at index of row is not valid for rules, remove it from legend
    for k, v in rules_dict.items():
        if n not in v:
            legend[index].remove(k)


for i in list_of_valid_tickets:
    list_of_n = [(index, int(x)) for index, x in enumerate(i.split(","))]
    for index, n in list_of_n:
        remove_unmatches(index, n, rules_dict, legend)

legend = {k: v for k, v in sorted(legend.items(), key=lambda x: len(x[1]))}
fields = dict()

# after sort, first item in legend have only one rule.
# remove with iteration from any other list in legend.
for k, v in legend.items():
    fields[k] = v[0]
    to_remove = v[0]
    for k, v in legend.items():
        if to_remove in v:
            v.remove(to_remove)

departures = {k: v for k, v in fields.items() if v.startswith("departure")}
my_ticket = my_ticket.split(",")

product = 1
for i in departures:
    product *= int(my_ticket[i])

print(product)
