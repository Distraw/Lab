from online_course import OnlineCourse
from course_material import CourseMaterial
from video_lesson import VideoLesson
from quiz import Quiz

from datetime import timedelta

if __name__ == '__main__':
    course_material1 = CourseMaterial(1, 'Material1')
    video_lesson1 = VideoLesson(2, 'Video1', timedelta(hours=1, minutes=30, seconds=30), 'my_url.com')
    quiz1 = Quiz(3, 'Quiz1', ['What`s your name?', 'How old are you?', 'What are your hobbies?'], 30)

    online_course1 = OnlineCourse()
    online_course1.add_material(course_material1)
    online_course1.add_material(video_lesson1)
    online_course1.add_material(quiz1)

    online_course1.display_course_structure()