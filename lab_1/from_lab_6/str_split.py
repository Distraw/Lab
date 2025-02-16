def str_split(input_str):
    i = 0
    while i < len(input_str):
        if input_str[i] == ' ':
            while i + 1 < len(input_str) and input_str[i + 1] == ' ':
                input_str = input_str[:i + 1] + input_str[i + 2:]

        i += 1

    return input_str