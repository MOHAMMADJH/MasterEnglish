from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from english.models import Question, Quiz, Lesson, Student, Teacher
from english.serializers import QuestionSerializer, QuizSerializer, LessonSerializer, UserSerializer, StudentSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView,
               AuthTokenSerializer):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)






class QuestionAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = QuestionSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = QuestionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            # question = Question.objects.get(id=dict(request.data)['statement'][0])
            # token = Token.objects.create(user=user)
            # print(token.key)
            serializer.save()
            # convert_speech_to_text(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = QuizSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = QuizSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            # question = Question.objects.get(id=dict(request.data)['statement'][0])
            # token = Token.objects.create(user=user)
            # print(token.key)
            serializer.save()
            # convert_speech_to_text(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Lesson.objects.get(id=pk)
        except Lesson.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = LessonSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = LessonSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            # question = Question.objects.get(id=dict(request.data)['statement'][0])
            # token = Token.objects.create(user=user)
            # print(token.key)
            serializer.save()
            # convert_speech_to_text(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class StudentAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_object(self, pk):
    #     try:
    #         return Student.objects.get(id=pk)
    #     except Student.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = StudentSerializer(snippet)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = StudentSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def post(self, request, format=None):
    #     print(dict(request.data))
    #     serializer = LessonSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # question = Question.objects.get(id=dict(request.data)['statement'][0])
    #         # token = Token.objects.create(user=user)
    #         # print(token.key)
    #         serializer.save()
    #         # convert_speech_to_text(request=request)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        stu = Student(user=user)
        stu.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class TeacherAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tea = Teacher(user=user)
        tea.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

def get_question_quiz(pk):
    qq = Question.object.all(quiz=pk)
