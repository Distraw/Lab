from person import Person

class Student(Person):
    def __init__(self, name : str, age : int, gender : str, university : str = None,
                 degree : str = None, year : int = None):
        super().__init__(name, age, gender)
        self._university = university
        self._degree = degree
        self._year = year

    def __str__(self):
        return super().__str__() + (f'\nUniversity: {self._university}'
                                    f'\nDegree: {self._degree}'
                                    f'\nYear: {self._year}')

    @property
    def university(self):
        return self._university

    @university.setter
    def university(self, value):
        self._university = value

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 0 or value > 6:
            raise ValueError('Year must be between 0 and 6')
        self._year = value