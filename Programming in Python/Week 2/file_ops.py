def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def read_file_into_list(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line)
    return lines



def write_first_line_to_file(file_contents, output_filename):
    data = file_contents.split('\n', 1)[0]

    with open(output_filename, 'w') as w_file:
        w_file.write(data)



def read_even_numbered_lines(file_name):
    even_data = []
    with open(file_name, 'r') as file:
        data = file.readlines()
        for idx, line in enumerate(data, 1):
            if idx % 2 == 0:
                even_data.append(idx)
    return even_data


def read_file_in_reverse(file_name):
    reversed_data = []
    with open(file_name, 'r') as file:
        for line in file:
            reversed_data.append(line)
    
    lines_list = []
    while reversed_data:
        lines_list.append(reversed_data.pop())
    
    for line in lines_list:
        print(line)

    return lines_list


def main():
    file_contents = read_file("sampletext.txt")
    print(file_contents)
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))
if __name__ == "__main__":
    main()
