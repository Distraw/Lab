def get_crime_data():
    rows = int(input("Введіть кількість видів злочинів: "))
    sentence_name = [""] * rows

    cols = int(input("Введіть кількість років: "))
    data = [[0] * cols for i in range(rows)]

    for i in range(rows):
        sentence_name[i] = input("Вид злочину " + str(i + 1) + ": ")
        for j in range(cols):
            data[i][j] = int(input("N" + str(j + 1) + ": "))

    return data, sentence_name

def get_max_increase(data):
    rows = len(data)

    max_increase = (data[0][len(data[0]) - 1] - data[0][0]) / data[0][0]
    max_id = 0
    for i in range(rows):
        current_increase = (data[i][len(data[i]) - 1] - data[i][0]) / data[i][0]
        if current_increase > max_increase:
            max_increase = current_increase
            max_id = i

    return max_increase, max_id