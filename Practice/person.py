class Person:
    def __init__(self, name : str, age : int, gender : str):
        self._name = name
        self._age = age
        self._gender = gender

    def __str__(self):
        return f'{self._name}, age: {self._age}, gender: {self._gender}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name : str):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age > 150:
            raise ValueError('age must be between 0 and 150')
        self._age = new_age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender : str):
        self._gender = new_gender