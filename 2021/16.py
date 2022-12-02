from functools import reduce

list_numeri = []

def handle_literal(counter, rest, inside_op=True):
    flag = False
    number_list = ""
    while not flag:
    # literal
        header, number, rest = rest[0:1], rest[1:5], rest[5:]
        counter += 5
        number_list += number
        # start with a 0 (last group
        if header == "0":
            flag = True
    
    value = int(number_list, 2)
    
    if counter % 4 != 0 and not inside_op:
        counter = ((counter//4)+1)*4
        rest = rest[24:]
    
    return rest, counter, value

def handle_operator(counter, rest):
    length_type, rest = rest[0], rest[1:]
    counter += 1

    values = []

    if length_type == '0':
        # prossimi 15 sono la lunghezza in bit dei sottopacchetti contenuti
        length, rest = int(rest[:15], 2), rest[15:]
        counter += 15
        while length > 0:
            rest, counter, length, _, value = parse(rest, counter, remaining_lenght=length, inside_op=True)
            values.append(value)
    else:
        packets, rest = int(rest[:11], 2), rest[11:]
        counter += 11
        while packets > 0:
            rest, counter, _, packets, value = parse(rest, counter, remaining_packets=packets, inside_op=True)
            values.append(value)

    return rest, counter, values

def parse(rest, counter = 0, remaining_lenght = None, remaining_packets = None, inside_op=False):
    old_counter = counter

    packet_version, rest = rest[0:3], rest[3:]
    packet_type_id, rest = rest[0:3], rest[3:]

    list_numeri.append(int(packet_version, 2))

    counter += 6
    value = None

    if packet_type_id == "100":
        rest, counter, value = handle_literal(counter, rest, inside_op=True)
    else:
        rest, counter, values = handle_operator(counter, rest)

        if int(packet_type_id, 2) == 0:
            value = sum(values)
        if int(packet_type_id, 2) == 1:
            value = reduce((lambda x, y: x * y), values)
        if int(packet_type_id, 2) == 2:
            value = min(values)
        if int(packet_type_id, 2) == 3:
            value = max(values)
        if int(packet_type_id, 2) == 5:
            if values[0] > values[1]:
                value = 1
            else:
                value = 0
        if int(packet_type_id, 2) == 6:
            if values[0] < values[1]:
                value = 1
            else:
                value = 0
        if int(packet_type_id, 2) == 7:
            if values[0] == values[1]:
                value = 1
            else:
                value = 0

    if remaining_lenght is not None:
        remaining_lenght -= (counter - old_counter)
    if remaining_packets is not None:
        remaining_packets -= 1

    return rest, counter, remaining_lenght, remaining_packets, value


def transform_input(inputt):
    def mapping(charr):
        if charr == '0':
            return '0000'
        if charr == '1':
            return '0001'
        if charr == '2':
            return '0010'
        if charr == '3':
            return '0011'
        if charr == '4':
            return '0100'
        if charr == '5':
            return '0101'
        if charr == '6':
            return '0110'
        if charr == '7':
            return '0111'
        if charr == '8':
            return '1000'
        if charr == '9':
            return '1001'
        if charr == 'A':
            return '1010'
        if charr == 'B':
            return '1011'
        if charr == 'C':
            return '1100'
        if charr == 'D':
            return '1101'
        if charr == 'E':
            return '1110'
        if charr == 'F':
            return '1111'

    foo = [mapping(x) for x in inputt]
    return "".join(foo)

inputt = transform_input("")
rest = inputt
_, _, _, _, value = parse(rest, 0)

print(sum(list_numeri))
print(value)
