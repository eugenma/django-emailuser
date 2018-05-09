from django.core import mail
from django.test import TestCase

from .factories import EmailUserFactory


class EmailUserTest(TestCase):
    def setUp(self):
        self.owner = EmailUserFactory()

    def test_fullname(self):
        expected = '{0} {1}'.format(self.owner.first_name, self.owner.last_name)

        received = self.owner.get_full_name()
        self.assertEqual(received, expected)

    def test_get_short_name(self):
        self.assertEqual(self.owner.get_short_name(), self.owner.first_name)

    def test_email_user(self):
        expected_subject = 'My Subject'
        expected_message = 'My Message'
        expected_from_email = 'asdf@fdsa.com'

        self.owner.email_user(expected_subject, expected_message, expected_from_email)

        self.assertEqual(len(mail.outbox), 1)

        send_email = mail.outbox[0]
        self.assertEqual(send_email.subject, expected_subject)
        self.assertEqual(send_email.body, expected_message)
        self.assertEqual(send_email.from_email, expected_from_email)
        self.assertIn(self.owner.email, send_email.to)

