from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django import forms
import random


from django.urls import reverse_lazy, reverse

from .models import Question, Attempt, Exam, Answer
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .forms import TestingForm, FirstQuestionForm


# Create your views here.
class MainView(CreateView):
    model = Attempt
    fields = ()
    success_url = reverse_lazy('civics:test2')
    template_name = 'exam_app/index.html'

    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        return super(MainView, self).form_valid(form)

    def get_success_url(self):
        attempt = Attempt.objects.get(pk=self.pk)
        print(attempt)
        exams = Exam.objects.filter(attempt=attempt)
        exam = exams.first()
        print(exam)
        pk = exam.pk
        print(pk)
        return reverse_lazy('civics:test2', kwargs={'pk': pk})


class StartExam(UpdateView):
    model = Exam
    form_class = FirstQuestionForm

    success_url = reverse_lazy('civics:answer2')
    template_name = 'exam_app/test2.html'

    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        print('self.pk_1', self.pk)
        return super(StartExam, self).form_valid(form)

    def get_success_url(self):
        print('self.pk_2', self.pk)
        exam = Exam.objects.get(pk=self.pk)
        pk = exam.pk
        print('exam.pk', pk)
        return reverse_lazy('civics:answer2', kwargs={'pk': pk})


class Answer(DetailView):
    model = Exam
    template_name = 'exam_app/answer2.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Exam, pk=self.id)

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['next_pk'] = self.id + 1
        return context



