import pandas as pd
import random
from datetime import date
from datetime import datetime

data = pd.DataFrame({
    'ID': random.sample(range(1000, 9000), 10),
    'Registration date': [date(random.randint(2010, 2026),
                               random.randint(1, 12),
                               random.randint(1, 28)) for _ in range(10)],
    'Age': [random.randint(13, 100) for _ in range(10)],
    'Gender': [random.choice(['Male', 'Female']) for _ in range(10)],
    'Country': [random.choice(['Ukraine', 'USA', 'France', 'Poland', 'Germany']) for _ in range(10)],
    'Frequency': [random.randint(1, 24) for _ in range(10)]
})

print('Original data:\n', data)
print('\n')

# Вік користувачів
max_age = data['Age'].max()
min_age = data['Age'].min()
avg_age = data['Age'].mean()

print('Max age: ', max_age)
print('Min age: ', min_age)
print('Avg age: ', avg_age)

# Найпопулярніший у країні
most_common = data['Country'].value_counts().idxmax()
print('Most popular in country: ', most_common)

# Сортування за частотою використання
data = data.sort_values(by='Frequency', ascending=True)
print(data.tail(5))

# Вилучити рядок із заданим номером
while True:
    try:
        row_to_delete = int(input("\nRow # to delete: "))
        data.drop(row_to_delete, inplace=True)
        break
    except:
        print("Invalid input, try again")

# Додати новий рядок
while True:
    try:
        new_id = data['ID'].max() + 1
        new_date = datetime.strptime(input("\nNew date: "), "%d-%m-%Y").date()
        new_age = int(input("New age: "))
        new_gender = input("New gender: ")
        new_country = input("Country: ")
        new_frequency = int(input("New frequency: "))

        data.loc[data.index.max() + 1] = [new_id, new_date, new_age, new_gender, new_country, new_frequency]
        break
    except:
        print("Invalid input, try again")

print('\nFinal dataframe:\n', data)