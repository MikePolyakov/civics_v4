from django.core.management.base import BaseCommand
from exam_app.models import Subject, SubjectPart, Student, Question, Answer, Chapter


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создание
        Student.objects.create(student_name='Any user')
        subject = Subject.objects.create(subject_name='Civics Questions for the Naturalization Test')

        part_1 = SubjectPart.objects.create(part_name='AMERICAN GOVERNMENT',
                                            subject=subject)

        chapter_a = Chapter.objects.create(chapter_name='A: Principles of American Democracy',
                                           part=part_1)

        question = Question.objects.create(question_name='What is the supreme law of the land?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='the Constitution',
                                       question=question)

        question = Question.objects.create(question_name='What does the Constitution do?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='sets up the government',
                                       question=question)
        answer = Answer.objects.create(answer_name='defines the government',
                                       question=question)
        answer = Answer.objects.create(answer_name='protects basic rights of Americans',
                                       question=question)

        question = Question.objects.create(question_name='The idea of self-government is in the first three words of '
                                                         'the Constitution. What are these words?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='We the People',
                                       question=question)

        question = Question.objects.create(question_name='What is an amendment?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='a change (to the Constitution)',
                                       question=question)
        answer = Answer.objects.create(answer_name='an addition (to the Constitution)',
                                       question=question)

        question = Question.objects.create(question_name='What do we call the first ten amendments to the Constitution?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='the Bill of Rights',
                                       question=question)

        question = Question.objects.create(question_name='What is one right or freedom from the First Amendment?*',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='speech',
                                       question=question)
        answer = Answer.objects.create(answer_name='religion',
                                       question=question)
        answer = Answer.objects.create(answer_name='assembly',
                                       question=question)
        answer = Answer.objects.create(answer_name='press',
                                       question=question)
        answer = Answer.objects.create(answer_name='petition the government',
                                       question=question)

        question = Question.objects.create(question_name='How many amendments does the Constitution have?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='twenty-seven (27)',
                                       question=question)

        question = Question.objects.create(question_name='What did the Declaration of Independence do?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='announced our independence (from Great Britain)',
                                       question=question)
        answer = Answer.objects.create(answer_name='declared our independence (from Great Britain)',
                                       question=question)
        answer = Answer.objects.create(answer_name='said that the United States is free (from Great Britain)',
                                       question=question)

        question = Question.objects.create(question_name='What are two rights in the Declaration of Independence?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='life',
                                       question=question)
        answer = Answer.objects.create(answer_name='liberty',
                                       question=question)
        answer = Answer.objects.create(answer_name='pursuit of happiness',
                                       question=question)

        question = Question.objects.create(question_name='What is freedom of religion?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='You can practice any religion, or not practice a religion.',
                                       question=question)

        question = Question.objects.create(question_name='What is the economic system in the United States?*',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='capitalist economy',
                                       question=question)
        answer = Answer.objects.create(answer_name='market economy',
                                       question=question)

        question = Question.objects.create(question_name='What is the “rule of law”?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_a)
        answer = Answer.objects.create(answer_name='Everyone must follow the law.',
                                       question=question)
        answer = Answer.objects.create(answer_name='Leaders must obey the law.',
                                       question=question)
        answer = Answer.objects.create(answer_name='Government must obey the law.',
                                       question=question)
        answer = Answer.objects.create(answer_name='No one is above the law.',
                                       question=question)

        chapter_b = Chapter.objects.create(chapter_name='B: System of Government',
                                           part=part_1)

        question = Question.objects.create(question_name='Name one branch or part of the government.*',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='Congress',
                                       question=question)
        answer = Answer.objects.create(answer_name='legislative',
                                       question=question)
        answer = Answer.objects.create(answer_name='President',
                                       question=question)
        answer = Answer.objects.create(answer_name='executive',
                                       question=question)
        answer = Answer.objects.create(answer_name='the courts',
                                       question=question)
        answer = Answer.objects.create(answer_name='judicial',
                                       question=question)

        question = Question.objects.create(
            question_name='What stops one branch of government from becoming too powerful?',
            subject=subject,
            part=part_1,
            chapter=chapter_b)

        answer = Answer.objects.create(answer_name='checks and balances',
                                       question=question)
        answer = Answer.objects.create(answer_name='separation of powers',
                                       question=question)

        question = Question.objects.create(
            question_name='Who is in charge of the executive branch?',
            subject=subject,
            part=part_1,
            chapter=chapter_b)
        answer = Answer.objects.create(answer_name='the President',
                                       question=question)

        question = Question.objects.create(question_name='Who makes federal laws?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='Congress',
                                       question=question)
        answer = Answer.objects.create(answer_name='Senate and House (of Representatives)',
                                       question=question)
        answer = Answer.objects.create(answer_name='(U.S. or national) legislature',
                                       question=question)

        question = Question.objects.create(question_name='What are the two parts of the U.S. Congress?*',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='the Senate and House (of Representatives)',
                                       question=question)

        question = Question.objects.create(question_name='How many U.S. Senators are there?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='one hundred (100)',
                                       question=question)

        question = Question.objects.create(question_name='We elect a U.S. Senator for how many years?',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='six (6)',
                                       question=question)

        question = Question.objects.create(question_name='Who is one of your state’s U.S. Senators now?*',
                                           subject=subject,
                                           part=part_1,
                                           chapter=chapter_b)
        answer = Answer.objects.create(answer_name='Answers will vary.',
                                       question=question)

        chapter_c = Chapter.objects.create(chapter_name='C: Rights and Responsibilities',
                                           part=part_1)
        part_2 = SubjectPart.objects.create(part_name='AMERICAN HISTORY',
                                            subject=subject)
        chapter_a = Chapter.objects.create(chapter_name='A: Colonial Period and Independence',
                                           part=part_2)
        chapter_b = Chapter.objects.create(chapter_name='B: 1800s',
                                           part=part_2)
        chapter_c = Chapter.objects.create(chapter_name='C: Recent American History and Other Important Historical '
                                                        'Information',
                                           part=part_2)
        part_3 = SubjectPart.objects.create(part_name='INTEGRATED CIVICS',
                                            subject=subject)
        chapter_a = Chapter.objects.create(chapter_name='A: Geography',
                                           part=part_3)
        chapter_b = Chapter.objects.create(chapter_name='B: Symbols',
                                           part=part_3)
        chapter_c = Chapter.objects.create(chapter_name='C: Holidays',
                                           part=part_3)

        print("-------")
        questions = Question.objects.all()
        for each in questions:
            print(each)
        print("-------")
        questions2 = Question.objects.filter(subject=1)
        for each in questions2:
            print(each)
        print("-------")
        q = Question.objects.first()
        print(q)
        print(q.subject)
        print("-------")
        print(SubjectPart.objects.get(id=1))
        print("-------")
        groups = SubjectPart.objects.all()
        for each in groups:
            print(each)
        print("-------")
