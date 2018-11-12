from django.test import TestCase
from .models import Program
from datetime import datetime, timedelta


class TestProgram(TestCase):
    def setUp(self):
        now = datetime.now()
        end = now + datetime.timedelta(minutes = 10)
        Program.objects.create(name='Fluminense', ptype=2, end=end)

    def test_program_is_live(self):
        f = Program.objects.get(name='Fluminense')
        self.assertEqual(f.is_live(), True)

    def test_radio_is_globo(self):
        f = Program.objects.get(name='Fluminense')
        self.assertEqual(f.radio, 1)

    def test_p_type_name(self):
        f = Program.objects.get(name='Fluminense')
        self.assertEqual(f.ptype, 2)