class CourseMaterial:
    def __init__(self, _id: int, name: str):
        self._id = _id
        self._name = name

    def display_content_info(self):
        print(f'Курс №{self._id}: \'{self._name}\'')