from course_material import CourseMaterial

from typing import override

class Quiz(CourseMaterial):
    def __init__(self, _id: int, name: str, questions: list, max_mark: int):
        super().__init__(_id, name)
        self._questions = questions
        self._max_mark = max_mark

    @override
    def display_content_info(self):
        super().display_content_info()
        print(f'Questions: {self._questions}\nMax mark: {self._max_mark}')