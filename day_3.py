from common_functions import load_as_string_array

def part_1():
    print("starting!")
    data = load_as_string_array('data/day_3_data.txt')
    final_score = 0
    for line in data:
        midpoint = int(len(line) / 2)
        str1 = set(line[:midpoint])
        str2 = set(line[midpoint:])
        letter = list(str1.intersection(str2))[0]
        print(str1)
        print(str2)
        print('--------')
        print()
        print("============")
        score = 0
        if letter.isupper():
            score = ord(letter) - 64
            score += 26
        else:
            score = ord(letter) - 96
        print(letter + " " + str(score))
        final_score += score
    print("---------------")
    print("---------------")
    print(final_score)


if __name__ == '__main__':
    data = load_as_string_array('data/day_3_data.txt')
    final_score = 0
    len_data = len(data)
    i = 0
    while i < len_data:
        l1 = data[i]
        l2 = data[i+1]
        l3 = data[i+2]
        intersection = set(l1).intersection(l2)
        intersection = intersection.intersection(l3)
        letter = list(intersection)[0]
        score = 0
        if letter.isupper():
            score = ord(letter) - 64
            score += 26
        else:
            score = ord(letter) - 96
        print(letter + " " + str(score))
        final_score += score
        print(intersection)
        print("------------")
        i += 3
    print("============")
    print(final_score)