from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionMethodTests(TestCase):
	def test_was_published_recently(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # def test_index_view_with_a_past_question(self):
    #     """
    #     Questions with a pub_date in the past should be displayed on the
    #     index page.
    #     """
    #     create_question(question_text="Past question.", days=-30)
    #     response = self.client.get(reverse('polls:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         ['<Question: Past question.>']
    #     )