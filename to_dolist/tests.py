from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task.title)

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_add_task_view(self):
        response = self.client.post('/add/', {'title': 'New Task'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, 'New Task')

