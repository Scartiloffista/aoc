import pathlib

path = pathlib.Path('.').parent / "inputs/16.txt"
with open(path, "r") as f:
    rules, my_ticket, nearby_tickets = f.read().split("\n\n")

my_ticket: str = my_ticket.splitlines()[1]
nearby_tickets: str = nearby_tickets.splitlines()[1:]

ranges: list = [x.split(": ")[1].split(" or ") for x in rules.splitlines()]
ranges: list = [item for sublist in ranges for item in sublist]

ranges_set: set = set()

for i in ranges:
    start, end = i.split("-")
    start, end = int(start), int(end)+1
    ranges_set |= set(range(start, end))

list_of_valid_tickets = []
for i in nearby_tickets:
    numbers_in_ticket: set = {int(x) for x in i.split(",")}
    if not numbers_in_ticket.issubset(ranges_set):
        list_of_valid_tickets.append(i)



        

print("ciao")