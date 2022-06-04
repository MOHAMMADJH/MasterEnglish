from rest_framework import serializers
from rest_framework.fields import FileField
from rest_framework.reverse import reverse
from english.models import Question, Quiz, Answer, Lesson, Content, User, Student, Teacher
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializer()
        id = serializers.IntegerField(source='user.id')
        username = serializers.CharField(source='user.username')
        email = serializers.EmailField(source='user.email')

        model = Student
        fields = ('id', 'username', 'email')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializer()
        id = serializers.IntegerField(source='user.id')
        username = serializers.CharField(source='user.username')
        email = serializers.EmailField(source='user.email')

        model = Teacher
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        audio_file = FileField()
        model = Content
        fields = ['id', 'content_name', 'audio_file', 'video_content']


class LessonSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='quiz-api',
    #     lookup_field='pk'
    # )

    class Meta:
        audio_file = FileField()
        model = Lesson
        fields = ['id', 'lesson_name', 'exercises', 'objective', 'quiz', 'content','endpoint']
    #
    # def get_url(self, obj):
    #     request = self.context.get('request')  # self.request
    #     if request is None:
    #         print('nnnnnnnn')
    #         return None
    #     return reverse("quiz-api", kwargs={"pk": obj.quiz.pk}, request=request)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        audio_file = FileField()
        model = Answer
        fields = ['answer', 'question', ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)


    class Meta:
        audio_file = FileField()
        model = Question
        fields = ['question_type', 'quiz', 'question', 'is_active', 'audio_file', 'category', 'answer', ]



class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)
    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-detail'
    # )


    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'question','endpoint']

    # def get_url(self):
    #     return f"http://127.0.0.1:8000/QuizAPI/{obj.pk}/"


    # def get_edit_url(self, obj):
    #     request = self.context.get('request')  # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
# factory = APIRequestFactory()
# request = factory.get('/')
# serializer_context = {
#     'request': Request(request),
# }
# p = Quiz.objects.first()
# s = QuizSerializer(instance=p, context=serializer_context)
# print (s.data)

