from django.test import TestCase
from django.core import mail
from eventex.subscriptions.forms import SubscriptionForm

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
            name="Robson Fernandes", cpf="12345678901", email='robson@gmail.com',
            phone='31-98816-2342'
        )
        self.client.post("/inscricao/", data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de Inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = "contato@eventex.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'robson@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscribe_email_body(self):

        contents = [
            'Robson Fernandes', '12345678901',
            'robson@gmail.com', '31-98816-2342'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
