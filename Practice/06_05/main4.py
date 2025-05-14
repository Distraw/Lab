if __name__ == '__main__':
    with open('test.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        print('Кількість символів у файлі: ', len(data))

        f.seek(0)

        strings = f.readlines()
        longest_string = max(strings, key=len)
        shortest_string = min(strings, key=len)

        if longest_string[len(longest_string) - 1] == '\n':
            longest_string = longest_string[:len(longest_string) - 1]

        if shortest_string[len(shortest_string) - 1] == '\n':
            shortest_string = shortest_string[:len(shortest_string) - 1]

        print('Найдовший рядок: \"', longest_string, '\", довжина ', len(longest_string))
        print('Найкоротший рядок: \"', shortest_string, '\", довжина ', len(shortest_string))