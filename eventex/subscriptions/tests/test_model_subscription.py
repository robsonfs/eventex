from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModeltest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name="Robson Fernandes",
            cpf="12345678901",
            email="robfds@gmail.com",
            phone="31-988162342"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_cretead_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
