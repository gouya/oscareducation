# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Rating.models import *
from django.test import TestCase
from resources.models import *


class Star_rating_TestCase(TestCase):
    def setUp(self):
        d = datetime
        u = User.objects.create()
        r = Resource.objects.create(section="test",content='{"kind": "lesson", "title": "Fonctions de référence", "author": "Paul Robaux"}  ')
        o = Star_rating.objects.create(
            star=2,
            resource=r,
            rated_by=u,
            rated_on="2017-02-18 10:10",
        )
        self.date = d
        self.id= o.id

    def test_star_in_table(self):
        star_r = Star_rating.objects.get(id=self.id)
        self.assertEqual(star_r.star,2)
        self.assertEqual(star_r.id,1)

# Tests for the class Answer
class Answer_TestCase(TestCase):
    def setUp(self):
        self.ob1 = Answer.objects.create(answer_statement = "Nous sommes le 31 octobre")
        self.ob2 = Answer.objects.create(answer_statement = " Yes we can")


    def test_answer_in_table(self):
        ans1 = Answer.objects.get(pk=self.ob1.id)
        self.assertEqual(ans1.answer_statement, "Nous sommes le 31 octobre")    # True
        ans2 = Answer.objects.get(pk=self.ob2.id)
        self.assertEqual(ans2.answer_statement, " Yes we can")                  # False


# Tests for the class Questin
class Question_TestCase(TestCase):
    def setUp(self):
        self.ob3 = Question.objects.create(question_statement = "Quel date sommes-nous?", type = 0)
        self.ob4 = Question.objects.create(question_statement = "Can we do this ?", type = 1)

    def test_question_in_table(self):
        ques1 = Question.objects.get(pk=self.ob3.id)
        self.assertEqual(ques1.question_statement, "Quel date sommes-nous?")  # True
        self.assertEqual(ques1.type, 0)                                       # True
        ques2 = Question.objects.get(pk=self.ob4.id)
        self.assertEqual(ques2.question_statement, "Can we do this ?")    # False
        self.assertEqual(ques2.type, 1)
        # False