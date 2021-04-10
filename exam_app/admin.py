from django.contrib import admin
from .models import Answer, Attempt, Subject, Student, SubjectPart, Chapter, Question, Exam

# Register your models here.
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Chapter)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(SubjectPart)
admin.site.register(Subject)
