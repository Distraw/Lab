from course_material import CourseMaterial

from typing_extensions import override
from datetime import timedelta

class VideoLesson(CourseMaterial):
    def __init__(self, _id: int, name: str, duration: timedelta, url: str):
        super().__init__(_id, name)

        self._id = _id
        self._name = name
        self._duration = duration
        self._url = url

    @override
    def display_content_info(self):
        super().display_content_info()
        print(f'Url: {self._url}\nDuration: {self._duration}')