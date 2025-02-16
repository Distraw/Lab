term_dictionary = {}

def process_command(command):
    sep_command = command.split()

    if len(sep_command) == 0:
        return "No command was given"

    if len(sep_command) == 1:
        if sep_command[0] == "exit":
            return 0
        else:
            return "Unknown command"

    elif len(sep_command) == 2:
        if sep_command[0] == "get":
            if sep_command[1] == "all":
                return "\n".join(f"{k}: {" ".join(map(str, v))}" for k, v in term_dictionary.items())

            elif sep_command[1] in term_dictionary:
                return " ".join(map(str, term_dictionary[sep_command[1]]))
            else:
                return "No such element in dictionary"

        elif sep_command[0] == "del":
            if sep_command[1] == "all":
                term_dictionary.clear()
                return "All elements were deleted"
            elif sep_command[1] in term_dictionary:
                del term_dictionary[sep_command[1]]
                return "Element \"" + sep_command[1] + "\" was deleted"
            else:
                return "No such element in dictionary"
        else:
            return "Unknown command"

    elif len(sep_command) > 2:
        if sep_command[0] == "add":
            term_dictionary[sep_command[1]] = sep_command[2:]
            return "Element \"" + sep_command[1] + "\" was added"
        else:
            return "Unknown command"