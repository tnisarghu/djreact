from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Learn
# Create your tests here.
class learnModelTests(TestCase):
    def test_was_published_recently_with_future_learn(self):
        """
                was_published_recently() returns False for learns whose pub_date
                is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_learn = Learn(pub_date=time)
        self.assertIs(future_learn.was_published_recently(), False)

    def test_was_published_recently_with_old_learn(self):
        """
        was_published_recently() returns False for learns whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_learn = Learn(pub_date=time)
        self.assertIs(old_learn.was_published_recently(), False)

    def test_was_published_recently_with_recent_learn(self):
        """
        was_published_recently() returns True for learns whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_learn = Learn(pub_date=time)
        self.assertIs(recent_learn.was_published_recently(), True)


def create_learn(name, days):
    """
    Create a learn with the given  name` and published the
    given number of `days` offset to now (negative for learns published
    in the past, positive for learns that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Learn.objects.create(name=name, pub_date=time)


class LearnIndexViewTests(TestCase):
    def test_no_learn(self):
        """
        If no learns exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('learn:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No learns are available.")
        self.assertQuerysetEqual(response.context['latest_learn_list'], [])

    def test_past_learn(self):
        """
     learns with a pub_date in the past are displayed on the
        index page.
        """
        create_learn(name="Past learn.", days=-30)
        response = self.client.get(reverse('learn:index'))
        self.assertQuerysetEqual(
            response.context['latest_learn_list'],
            ['<Learn: Past learn.>']
        )

    def test_future_learn(self):
        """
     learns with a pub_date in the future aren't displayed on
        the index page.
        """
        create_learn(name="Future learn.", days=30)
        response = self.client.get(reverse('learn:index'))
        self.assertContains(response, "No learns are available.")
        self.assertQuerysetEqual(response.context['latest_learn_list'], [])

    def test_future_learn_and_past_learn(self):
        """
        Even if both past and future learns exist, only past learns
        are displayed.
        """
        create_learn(name="Past learn.", days=-30)
        create_learn(name="Future learn.", days=30)
        response = self.client.get(reverse('learn:index'))
        self.assertQuerysetEqual(
            response.context['latest_learn_list'],
            ['<Learn: Past learn.>']
        )

    def test_two_past_learn(self):
        """
        The learns index page may display multiple learns.
        """
        create_learn(name="Past learn 1.", days=-30)
        create_learn(name="Past learn 2.", days=-5)
        response = self.client.get(reverse('learn:index'))
        self.assertQuerysetEqual(
            response.context['latest_learn_list'],
            ['<Learn: Past learn 2.>', '<Learn: Past learn 1.>']
        )

class LearnDetailViewTests(TestCase):
    def test_future_learn(self):
        """
        The detail view of a learn with a pub_date in the future
        returns a 404 not found.
        """
        future_learn = create_learn(name='Future learn.', days=5)
        url = reverse('learn:detail', args=(future_learn.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_learn(self):
        """
        The detail view of a learn with a pub_date in the past
        displays the learn's text.
        """
        past_learn = create_learn(name='Past Learn.', days=-5)
        url = reverse('learn:detail', args=(past_learn.id,))
        response = self.client.get(url)
        self.assertContains(response, past_learn.name)