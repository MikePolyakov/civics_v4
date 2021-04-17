from django.db import models
import random


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.student_name


class Attempt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, default=1, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField(default=20)
    min_to_pass = models.PositiveIntegerField(default=18)
    # result maybe 0
    result = models.IntegerField(default=0)

    # Переопределение метода save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not Exam.objects.filter(attempt=self).exists():
            questions = Question.objects.all()

            for i in range(20):
                random_question = random.choice(questions)
                blank_answer = Answer.objects.filter(answer_name='wrong answer').first()
                Exam.objects.create(attempt=self,
                                    question=random_question,
                                    answer=blank_answer)


class SubjectPart(models.Model):
    part_name = models.CharField(max_length=100, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.part_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=100, blank=True)
    part = models.ForeignKey(SubjectPart, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_name


class Question(models.Model):
    question_name = models.CharField(max_length=100, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    part = models.ForeignKey(SubjectPart, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.question_name


class Answer(models.Model):
    answer_name = models.CharField(max_length=100, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    is_correct = models.BooleanField(default=True)

    def __str__(self):
        return self.answer_name


class Exam(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
