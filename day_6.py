from common_functions import load_as_string_array

if __name__ == '__main__':
    data = load_as_string_array('data/day_6_data.txt')
    line = data[0]
    print(len(line))
    for i in range(13, len(line)):
        if(len(set(line[i-14:i])) == 14):
            print(i)
            break