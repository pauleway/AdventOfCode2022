
def load_input_as_int_array(file):
    with open(file) as f:
        text = f.readlines()
    return [int(row.strip()) for row in text]

def load_as_string_array(file):
    with open(file) as f:
        text = f.readlines()
    return [row.strip() for row in text]

def read_lines_until_line_break(file):
    with open(file) as f:
        text = f.readlines()
        print(len(text))
        last_num = 0
        arr = []
        for line in text:
            if line != '\n':
                last_num += int(line)
            else :
                arr.append(last_num)
                last_num = 0
        print(len(arr))
        return arr
