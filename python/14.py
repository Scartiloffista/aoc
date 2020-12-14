import pathlib

path = pathlib.Path('.').parent / "inputs/14.txt"
with open(path, "r") as f:
    instructions = [x.split(" = ") for x in f.read().splitlines()]

mem: dict = dict()
for instr, n in instructions:
    if instr == "mask":
        mask_and = int(n.replace("X", "1"), 2)
        mask_or = int(n.replace("X", "0"), 2)
    else:
        mem_loc = instr[4:-1]
        n_to_put = int(n) | mask_or
        n_to_put = n_to_put & mask_and
        mem[mem_loc] = n_to_put


val = sum(mem.values())
print(val)

## uuurgh, ugly
list_combs = []


def gen_masks(strr, index, list_combs):
    if index == len(strr):
        list_combs += [strr]
    elif strr[index] == "0":
        gen_masks(strr, index+1, list_combs)
    elif strr[index] == "1":
        gen_masks(strr, index+1, list_combs)
    else:
        gen_masks(strr.replace("X", "0", 1), index+1, list_combs)
        gen_masks(strr.replace("X", "1", 1), index+1, list_combs)


def replace_with_x(strr, list_pos):
    strr = list(strr[::-1])
    for (i, x) in enumerate(strr):
        if i in list_pos:
            strr[i] = "X"
    return "".join(strr[::-1])


mem: dict = dict()
for instr, n in instructions:
    if instr == "mask":
        mask = n
        list_pos = [i for i, x in enumerate(n[::-1]) if x == "X"]
        base_address = int(n.replace("X", "0"), 2)
    else:
        mem_loc = int(instr[4:-1])
        base_address |= mem_loc
        base_address_bin = bin(base_address)[2:]
        base_mask = replace_with_x(base_address_bin, list_pos)
        list_of_mem_loc = []
        gen_masks(base_mask, 0, list_of_mem_loc)
        list_of_mem_loc = [int(x, 2) for x in list_of_mem_loc]
        for i in list_of_mem_loc:
            mem[i] = int(n)

val = sum(mem.values())