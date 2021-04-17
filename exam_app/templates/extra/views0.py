from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import random

from django.urls import reverse_lazy, reverse

from exam_app.models import Question, Attempt, Exam, Answer
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from exam_app.forms import TestingForm


# Create your views here.
def civics(request):
    # if request.method == 'POST':
    #     hello(request)
    #     return render(request,
    #                   'exam_app/test.html',
    #                   {})
    # else:
    #     return render(request,
    #                   'exam_app/index.html',
    #                   {'value': 'Button clicked'})

    return render(request,
                  'exam_app/index.html',
                  context={})


def hello(request):
    print("hello")
    return render(request,
                  'exam_app/test.html',
                  {})


def test(request):
    print("++++")
    if request.method == 'GET':
        return render(request,
                      'exam_app/test.html',
                      {})


# def start(request):
#     if request.method == 'GET':
#             attempt = Attempt.objects.create()
#             attempt_id = attempt.id
#             print("attempt_id =", attempt_id)
#
#             questions = Question.objects.all()
#             random_question = random.choice(questions)
#             q_id = random_question.id
#             blank_answer = Answer.objects.get(answer_name='blank answer')
#
#             exam = Exam.objects.create(attempt=attempt,
#                                        question=random_question,
#                                        answer=blank_answer)
#
#             exam_id = exam.id
#             print("exam_id =", exam_id)
#             return render(request,
#                           'exam_app/test.html',
#                           context={
#
#                                    'exam': exam,
#
#                                    })




    # if request.method == 'POST':
    #     Attempt.objects.all().delete()
    #
    #     attempt = Attempt.objects.create()
    #     attempt_id = attempt.id
    #     print("attempt_id =", attempt_id)
    #
    #     questions = Question.objects.all()
    #     random_question = random.choice(questions)
    #     q_id = random_question.id
    #     blank_answer = Answer.objects.get(answer_name='blank answer')
    #
    #     exam = Exam.objects.create(attempt=attempt,
    #                                question=random_question,
    #                                answer=blank_answer)
    #
    #     exam_id = exam.id
    #     print("exam_id =", exam_id)
    #     return render(request,
    #                   'exam_app/index.html',
    #                   context={'exam_id': exam_id})

    #     url = 'exam_app/test/' + exam_id + '/'
    #     return HttpResponseRedirect(reverse("civics:test/"))


# def test(request, pk):
#     if request.method == 'GET':
#         exam = get_object_or_404(Exam, id=pk)
#
#         attempt_id = exam.attempt.id
#
#         attempt = Attempt.objects.get(id=attempt_id)
#         exams = Exam.objects.filter(attempt=attempt)
#         count = 0
#         for each in exams:
#             count += each.answer.is_correct
#
#         return render(request,
#                       'exam_app/test.html',
#                       context={'exam': exam,
#                                'count': count})
    # if request.method == 'POST':
    #
    #     return render(request,
    #                   'exam_app/answer.html',
    #                   context={})

    # if request.method == 'GET':
    #     test = get_object_or_404(Exam, id=id)
    #     return render(request, 'exam_app/test.html', context={'test': test})
    #
    # else:
    #     form = TestingForm(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('civics:index'))
    #     else:
    #         return render(request, 'exam_app/test.html', context={'form': form})

    # if request.method == 'POST':
    #     Attempt.objects.all().delete()
    #
    #     attempt = Attempt.objects.create()
    #     attempt_id = attempt.id
    #     print("attempt_id =", attempt_id)
    #
    #     questions = Question.objects.all()
    #     random_question = random.choice(questions)
    #     q_id = random_question.id
    #     blank_answer = Answer.objects.get(answer_name='blank answer')
    #
    #     exam = Exam.objects.create(attempt=attempt,
    #                                question=random_question,
    #                                answer=blank_answer)
    #
    #     exam_id = exam.id
    #     print("exam_id =", exam_id)
    # else:
    #     return render(request,
    #                   'exam_app/index.html',
    #                   context={})



