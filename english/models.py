# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from english.validators import validate_is_audio, validate_is_video


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    # class Meta:
    #     ordering = ('name', 'email',)
    # #
    # # USERNAME_FIELD = 'email'
    # # REQUIRED_FIELDS = ['username']


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_name

    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/LessonAPI/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    # @property
    # def path(self):
    #     return f"/QuizAPI/{self.pk}/"

    @property
    def question(self):
        return self.question_set.all()

class English(models.Model):
    """
    The first part Listening:
    """
    lesson_category= models.CharField(max_length=100,default="listening")

    def __str__(self):
        return self.lesson_category
class Lesson(models.Model):
    """
    lesson from listening and speaking
    """
    lesson_name = models.CharField(max_length=200)
    exercises = models.CharField(max_length=200)
    objective = models.TextField()
    exam_mark = models.FloatField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1)
    lesson_number = models.IntegerField(unique=True)
    category = models.ForeignKey(English,on_delete=models.CASCADE)


    def __str__(self):
        return self.lesson_name

    def get_absolute_url(self):
        endpoint = Student.stu_endpoint
        return f"http://127.0.0.1:8000/QuizAPI/{self.quiz.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def content(self):
        return self.content_set.all()


class Content(models.Model):
    content_name = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='musics/', validators=[validate_is_audio], null=True)
    video_content = models.FileField(upload_to='video/', null=True, validators=[validate_is_video])
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.content_name


# class LetsPractise(models.Model):
#     """
#     This part is for the interim calendar entitled (Let's practice).. It consists of three questions
#     """
#     questions = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.questions

class QuestionType(models.Model):
    question_type = models.CharField(max_length=50)
    mark = models.IntegerField(default=2)

    def __str__(self):
        return self.question_type


class QuestionCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Question(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=700, verbose_name='Question statement')
    is_active = models.BooleanField(default=True, verbose_name='Active',
                                    help_text='Should question be included in quiz?')
    audio_file = models.FileField(upload_to='musics/', validators=[validate_is_audio], null=True)
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, max_length=5,
                                 verbose_name='Category')

    def __str__(self):
        return self.question

    @property
    def match_answer(self):
        return self.questionsmatchanswer_set.all()

    @property
    def answer(self):
        return self.answer_set.all()

    class META:
        ordering = "id"


class Answer(models.Model):
    answer = models.CharField(max_length=200, null=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Choice(models.Model):
    choice = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class MultipleChoiceQuestion(models.Model):
    # answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice


class QuestionsMatchAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_match = models.CharField(max_length=200)
    b_match = models.CharField(max_length=200)

    def __str__(self):
        return self.question.question


class Student(models.Model):
    """r
    Student
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=1)
    current_lesson_status = models.BooleanField(default=False)

    def set_next_lesson(self):
        if self.current_lesson_status:
            self.current_lesson.pk = self.current_lesson.pk + 1
        return self.current_lesson.pk
        # self.current_lesson =

    @property
    def get_next_lesson(self):
        return self.current_lesson
    @property
    def stu_endpoint(self):
        return f"http://127.0.0.1:8000/LessonAPI/{self.current_lesson.pk}"

    def __str__(self):
        return str(self.user.username)


class Teacher(models.Model):
    """
    Teacher
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class StuMatchAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_match = models.CharField(max_length=200)
    b_match = models.CharField(max_length=200)

    def __str__(self):
        return self.a_match


class UserAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.answers.answer

    class Meta:
        ordering = ('student', 'questions',)


class QuestionMath(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class EnglishM(models.Model):
    lesson_name = models.CharField(max_length=200)
    directions = models.TextField()
    number_of_lessons = models.IntegerField
    mark = models.FloatField()
    final_calendar_mark = models.FloatField()

    def __str__(self):
        return self.lesson_name


class WarmUp(models.Model):
    """
    It is a picture or a short video with a question
    """
    warm_up_name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, default="avatar.svg")
    video = models.CharField(max_length=200)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.warm_up_name


class Course(models.Model):
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name


class StudentCourse(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_Date = models.DateTimeField()

    def __str__(self):
        return self.stu.name





class Topic(models.Model):
    name = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Contestant:
    pass


class Association:
    pass


class UsersTest:
    pass
