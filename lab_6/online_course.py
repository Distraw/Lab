from course_material import CourseMaterial
from video_lesson import VideoLesson
from quiz import Quiz

class OnlineCourse:
    def __init__(self):
        self._material = []

    def add_material(self, material: CourseMaterial):
        self._material.append(material)

    def display_course_structure(self):
        for material in self._material:
            material.display_content_info()
            print('\n')