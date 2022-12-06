from common_functions import load_as_string_array

if __name__ == '__main__':
    data = load_as_string_array('data/day_6_data.txt')
    line = data[0]
    print(len(line))
    for i in range(3, len(line)):
        if(len(set(line[i-4:i])) == 4):
            print(i)
            break