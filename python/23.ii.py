line = [1, 6, 7, 2, 4, 8, 3, 5, 9] + list(range(10, 1000001))
# line = [3, 8, 9, 1, 2, 5, 4, 6, 7]
n_of_elems = 1000000
max_val = 1000000
min_val = 1


class Node:
    # def __init__(self, value: int, pos: int, previous, next):
    def __init__(self, value, previous, next):
        self.value = value
        # self.pos = pos
        self.previous = previous
        self.next = next

    # def __init__(self, value: int, pos: int):
    def __init__(self, value):
        self.value = value
        # self.pos = pos


pos_nodes = [Node(0)] * n_of_elems  # pos -> Node
dict_labels = {}  # label -> Node
for i, x in enumerate(line):
    pos_nodes[i] = Node(x)
    dict_labels[x] = pos_nodes[i]

for i in range(0, n_of_elems):
    pos_nodes[i].previous = pos_nodes[(i - 1) % n_of_elems]
    pos_nodes[i].next = pos_nodes[(i + 1) % n_of_elems]

print("ciao")

counter = 0

pos = 0
for _ in range(100):
    current_cup = pos_nodes[pos]
    current_value = current_cup.value

    c1 = pos_nodes[(pos + 1) % n_of_elems]
    c2 = pos_nodes[(pos + 2) % n_of_elems]
    c3 = pos_nodes[(pos + 3) % n_of_elems]

    # cut from circle!
    current_cup.next = c3.next
    current_cup.next.previous = current_cup

    vals = [c1.value, c2.value, c3.value]
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

    # now i put cup after me
    destionation_cup = dict_labels[current_value]  # is a node
    old_next = destionation_cup.next

    # put 3 cups after destination
    destionation_cup.next = c1
    destionation_cup.next.previous = destionation_cup

    # put old next after 3 cups
    c3.next = old_next
    c3.next.previous = c3

    # reordering!

    new_pos = (pos + 1) % n_of_elems
    next_cup = current_cup.next
    while new_pos != pos:
        pos_nodes[new_pos] = next_cup
        next_cup = next_cup.next
        new_pos = (new_pos + 1) % n_of_elems

    pos = (pos + 1) % n_of_elems
    debug_line = [x.value for x in pos_nodes]

    counter += 1
    if (counter % 1000) == 0:
        print(counter)

#     destionation_cup.pop_element()
#     destionation_cup.previous = current_cup
#     destionation_cup.next = c1
#     current_cup.next = destionation_cup

#     next_node_to_change = destionation_cup
#     next_pos_to_change = (pos + 1) % 10

#     while True:
#         pos_nodes[next_pos_to_change] = next_node_to_change
#         next_pos_to_change = (next_pos_to_change + 1) % n_of_elems
#         next_node_to_change = next_node_to_change.next
#         if next_node_to_change == destionation_cup:
#             break

#     pos = (pos + 1) % 10

#     debug_line = [x.value for x in pos_nodes]

print(debug_line)