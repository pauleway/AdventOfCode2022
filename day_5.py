from common_functions import load_as_string_array


def carp_loader():
    arr = load_as_string_array('data/day_5_data.txt')
    stacks = {}
    for i in range(1, 9):
        stacks[i] = []
    # load the initial stacks
    for i in range(8):
        iterator = 1
        for j in range(0, 8):
            char_position = j * 4 + 1
            try:
                item = arr[i][char_position]
            except:
                item = ' '
            stacks[j + 1].insert(0, item)
    for item in stacks:
        print(stacks[item])
    print(stacks)

stacks = {
    1: ['W', 'B', 'D', 'N', 'C', 'F', 'J'],
    2: ['P', 'Z', 'V', 'Q', 'L', 'S', 'T'],
    3: ['P', 'Z', 'B', 'G', 'J', 'T'],
    4: ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C'],
    5: ['G', 'V', 'B', 'J', 'S'],
    6: ['P', 'S', 'Q'],
    7: ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N'],
    8: ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R'],
    9: ['V', 'D', 'T', 'R']
}

def part_1():
    for line in instructions:
        instructs = line.split(' ')
        amount = int(instructs[1])
        originator = int(instructs[3])
        destination = int(instructs[5])
        for item in range(amount):
            stacks[destination].append(stacks[originator].pop())
    final_answer = ""
    for item in range(1, 10):
        final_answer += stacks[item][-1]

    print(final_answer)
    for item in stacks:
        print(stacks[item])

if __name__ == '__main__':

    instructions = load_as_string_array('data/day_5_data.txt')
    instructions = instructions[10:]
    # part_1()
    for line in instructions:

        instructs = line.split(' ')
        amount = int(instructs[1])
        originator = int(instructs[3])
        destination = int(instructs[5])
        try:
            boxes = stacks[originator][-amount:]
            print(boxes)
        except:
            print(line)
            print(amount, stacks[originator], stacks[destination])

        stacks[originator] = stacks[originator][:-amount]
        for box in boxes:
            stacks[destination].append(box)

    final_answer = ""
    for item in range(1, 10):
        final_answer += stacks[item][-1]


    print(final_answer)
    for item in stacks:
        print(stacks[item])


