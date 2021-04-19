from django import forms
from .models import Attempt, Exam, Question, Answer
import random


class TestingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TestingForm, self).__init__(*args, **kwargs)

        self.fields['answer'].empty_label = None
        answers = Answer.objects.filter(question=self.instance.question.id)
        self.fields['answer'] = forms.ModelChoiceField(queryset=answers,
                                                       label=None,
                                                       widget=forms.RadioSelect())

    class Meta:
        model = Exam
        fields = ['answer']


class FirstQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FirstQuestionForm, self).__init__(*args, **kwargs)
        print(self.instance.attempt)
        print(self.instance.question)

        self.fields['answer'].empty_label = None
        answers = Answer.objects.filter(question=self.instance.question.id)
        self.fields['answer'] = forms.ModelChoiceField(queryset=answers,
                                                       label=None,
                                                       widget=forms.RadioSelect())

    class Meta:
        model = Exam
        fields = ['answer']

