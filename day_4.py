from common_functions import load_as_string_array


if __name__ == '__main__':
    stuff = load_as_string_array('data/day_4_data.txt')
    num_overlapping_pairs = 0
    for line in stuff:
        (pair_1, pair_2) = line.split(',')
        start_1, end_1 = pair_1.split('-')
        start_2, end_2 = pair_2.split('-')
        set_1 = set(range(int(start_1), int(end_1)+1))
        set_2 = set(range(int(start_2), int(end_2)+1))
        intersection = set_1.intersection(set_2)
        if(len(intersection)) > 0:
            num_overlapping_pairs += 1
        # if (start_1 >= start_2 and end_1 <= end_2) or (start_2 >= start_1 and end_2 <= end_1):
        # if set_1.issubset(set_2) or set_2.issubset(set_1):
        #     print('they are subsets!')
        #     print(pair_1, end='::')
        #     print(pair_2)
        #     print(set_1)
        #     print(set_2)
        #     num_overlapping_pairs += 1

    print(num_overlapping_pairs)

