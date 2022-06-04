from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from english.models import Content, Room, Topic, Message, Lesson, Listening, Speaking, WarmUp, Student, Teacher, StudentCourse, Course, QuestionCategory, User, Question, Quiz, Answer, UserAnswer, QuestionsMatchAnswer, StuMatchAnswer, QuestionType


# @admin.register(User)
# class MyUserAdmin(UserAdmin):
#     model = User
#     list_display = ('name', 'phone_number',
#                     'email')
#     list_filter = ('phone_number',
#                    'email')
#     search_fields = ('phone_number',)
#     ordering = ('phone_number',)
#     filter_horizontal = ()
    # I've added this 'add_fieldset'

@admin.register(Question)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("question", "quiz", "is_active", 'category')


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("quiz_name", )

@admin.register(Content)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("content_name", )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "is_correct", "question")


@admin.register(UserAnswer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "questions", "answers")


@admin.register(QuestionsMatchAnswer)
class QuestionsMatchAnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "a_match", "b_match")


@admin.register(StuMatchAnswer)
class StuMatchAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "a_match", "b_match")


admin.site.register(QuestionType)
admin.site.register(User)


admin.site.register(Room)
admin.site.register(Topic)
admin.site.register([
    Message, Lesson,
     Listening, Speaking,
    WarmUp, Student, Teacher,
    StudentCourse, Course])
admin.site.register([
    QuestionCategory])