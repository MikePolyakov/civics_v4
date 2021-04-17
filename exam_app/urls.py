from django.urls import path
from exam_app import views

app_name = 'exam_app'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('test2/<int:pk>/', views.StartExam.as_view(), name='test2'),
    path('answer2/<int:pk>/', views.Answer.as_view(), name='answer2'),



]
