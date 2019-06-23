import datetime, decimal, os
from django.test import TestCase, Client
from .models import *

# Create your tests here.

class ModelsTestCase(TestCase):

    def setUp(self):
        exec(open("calc/spx_data.py").read())

    def test_set_up(self):
        date = datetime.date(1999,1,1)
        retrun = Index.objects.get(id=1)
        self.assertEqual(retrun.index_name, 'VBMFX')

    def test_get_all(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/api/index/')
        self.assertEqual(Index.objects.all().count(),len(response.data))