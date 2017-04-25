from django.test import TestCase
from django.core import mail
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
    """Get /inscricao/ must return status code 200"""

    def setUp(self):
        self.resp = self.client.get("/inscricao/")

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, "subscriptions/subscription_form.html")

    def test_html(self):
        """HTML must contains input tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
            name="Robson Fernandes", cpf="12345678901", email='robson@gmail.com',
            phone='31-98816-2342'
        )
        self.resp = self.client.post("/inscricao/", data)

    def test_post(self):
        """Valid post should redirect to /incricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

class SubscribePostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "subscriptions/subscription_form.html")

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):

    def test_message(self):
        data = dict(name="Robson Fernandes", cpf="12345678901",
                    email="robfds@gmail.com", phone="31-98816-2342")
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, "Inscrição realizada com sucesso")
