from django.test import TestCase
from notes.models import Note
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class Test_Create_Note(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_note = Note.objects.create(text='This is a test note')

    def test_note_content(self):
        note = Note.objects.get(pk=1)
        text = f'{note.text}'
        self.assertEqual(text, 'This is a test note')
        self.assertEqual(str(note), 'This is a test note')

class NotesEndpointTest(APITestCase):

    def test_view_notes(self):
        response = self.client.get('http://localhost:8000/api/notes/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def create_note(self):
        test_note = {"text": "This is the post test note"}
        response = self.client.post('http://localhost:8000/api/notes/', test_note, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)



         





