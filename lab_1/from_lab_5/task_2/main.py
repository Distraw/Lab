import crime

while True:
    try:
        data, sentence_name = crime.get_crime_data()
        break
    except:
        print("Невірний формат даних! Спробуйте знову")

max_increase, max_id = crime.get_max_increase(data)

print("Вид злочину з найбільшим приростом злочинності: " + sentence_name[max_id])
print("Найбільший приріст за цим видом злочину: " + str(max_increase * 100) + "%")