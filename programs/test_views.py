from django.test import TestCase
from django.test import Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from datetime import datetime, timedelta
import pytz

from .models import Program


class TestViews(TestCase):
    client = Client()
    def setUp(self):
        timeZone = datetime.now(pytz.timezone("America/Sao_Paulo"))
        end = timeZone + timedelta(minutes = 10)
        Program.objects.create(name='Fluminense', ptype=2, end=end)
    
    def test_index_should_be_ok(self):
        resp = self.client.get(reverse("program:index"))
        self.assertEqual(resp.status_code, 200)

    def test_detail_should_be_ok(self):
        resp = self.client.get(reverse("program:detail", kwargs={'program_id':1}))
        self.assertEqual(resp.status_code, 200)

    def test_grid_should_be_ok(self):
        resp = self.client.get(reverse("programs:grid", kwargs={'grid_id':1}))
        self.assertEqual(resp.status_code, 200)