import database

while True:
    command = input("> ")
    result = database.process_command(command)

    if result == 0:
        break
    else:
        print(result)
