line = [1, 6, 7, 2, 4, 8, 3, 5, 9]  # + list(range(10, 1000001))
# line = [3, 8, 9, 1, 2, 5, 4, 6, 7]
n_of_elems = 1000000
max_val = 1000000
min_val = 1


class Node:
    def __init__(self, value, previous, next):
        self.value = value
        # self.pos = pos
        self.previous = previous
        self.next = next

    def __init__(self, value):
        self.value = value


dict_labels = {}


starting_node = Node(line[0])
dict_labels[line[0]] = starting_node

current_node = starting_node

for label in line[1:]:
    new_node = Node(label)
    dict_labels[label] = new_node
    new_node.previous = current_node
    current_node.next = new_node
    current_node = current_node.next

for label in range(10, 1000001):
    new_node = Node(label)
    dict_labels[label] = new_node
    new_node.previous = current_node
    current_node.next = new_node
    current_node = current_node.next

starting_node.previous = current_node
current_node.next = starting_node

current_cup = starting_node
for _ in range(0, 10 * 1000 * 1000):
    current_value = current_cup.value
    c1 = current_cup.next
    c2 = c1.next
    c3 = c2.next

    vals = [c1.value, c2.value, c3.value]

    # cutting!
    current_cup.next = c3.next
    current_cup.next.previous = current_cup

    flag = True
    current_value -= 1
    while flag:
        if current_value in vals:
            current_value -= 1
            if current_value < min_val:
                current_value = max_val
        else:
            if current_value == 0:
                current_value = max_val
            else:
                flag = False

    destionation_cup = dict_labels[current_value]  # is a node
    old_next = destionation_cup.next

    # put 3 cups after destination
    destionation_cup.next = c1
    destionation_cup.next.previous = destionation_cup

    # put old next after 3 cups
    c3.next = old_next
    c3.next.previous = c3

    current_cup = current_cup.next

print(dict_labels[1].next.value)
print(dict_labels[1].next.next.value)

print("ciao")
