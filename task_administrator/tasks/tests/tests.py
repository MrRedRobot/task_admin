from django.test import TestCase
from rest_framework import status

from rest_framework.test import RequestsClient, APITestCase
from django.urls import reverse

from tasks.models.task import Task
from tasks.models.comentary import Comentary

class CreateTestCase(APITestCase):

    def test_url_TaskListAPIView(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)

    def test_code_generation(self):
        #al ingresar comentarios en task si se estan visualizando
        task = Task.objects.create(
        name = 'Prueba',
        description = 'prueba',
        state = 'BACKLOG',
        priority = 'MEDIA',
        delivery_date = '2022-12-12'
        )
        self.assertIsNotNone(task)

    def test_code_generation(self):
        #al ingresar comentarios en task si se estan visualizando
        task = Task.objects.create(
        pk= '1',
        name = 'Prueba',
        description = 'prueba',
        state = 'BACKLOG',
        priority = 'MEDIA',
        delivery_date = '2022-12-12'
        )
        response = self.client.get("http://127.0.0.1:8000/apitasks/tasks/retrieve/1/")
        self.assertEqual(response.status_code, 200)