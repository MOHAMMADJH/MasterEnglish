"""MasterEnglish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views

from english.views import QuestionAPI, QuizAPI, LessonAPI, RegisterAPI, StudentAPI, TeacherAPI, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('QuestionAPI/<int:pk>/', QuestionAPI.as_view()),
    path('QuestionAPI/', QuestionAPI.as_view()),
    path('QuizAPI/<int:pk>/', QuizAPI.as_view()),
    path('StudentAPI/', StudentAPI.as_view()),
    path('TeacherAPI/', TeacherAPI.as_view()),
    path('LessonAPI/<int:pk>/', LessonAPI.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
