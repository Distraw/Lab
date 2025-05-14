if __name__ == '__main__':
    file1 = open('test.txt', 'a', encoding='utf-8')
    file2 = open('test.txt', 'a', encoding='utf-8')
    file3 = open('test.txt', 'r', encoding='utf-8')

    file1.write('hello ')

    print(file3.read())

    file2.write(' world')

    file1.close()
    file2.close()

