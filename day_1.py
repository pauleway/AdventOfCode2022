from common_functions import read_lines_until_line_break

if __name__ == '__main__':
    arr = read_lines_until_line_break('data/day_1_data.txt')
    arr = sorted(arr)
    print(arr)
    array_len = len(arr)
    output = 0
    for i in arr[-3:]:
        output += i
    print('FINAL')
    print(output)
