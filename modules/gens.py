def read_file_line_by_line(file_path, max_line_length):
    with open(file_path, 'r') as file:
        for line in file:
            if len(line) > max_line_length:
                start_index = 0
                while start_index < len(line):
                    yield line[start_index : start_index + max_line_length]
                    start_index += max_line_length
            else:
                yield line

file_path = ("ryba.txt")
max_line_length = 10

for truncated_line in read_file_line_by_line(file_path, max_line_length):
    print(truncated_line, end='')
