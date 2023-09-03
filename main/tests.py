from rest_framework import status
from rest_framework.test import APITestCase

class MainTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_lesson(self):
        """Тестирование создание уроков"""

        data={
            "lesson_name": "Matematica 38",
            "lesson_description": "Важнейший предмет в науках",
            "lesson_link": "https://youtube.com/",
            "well_name": 1
        }


        response = self.client.post(
            '/lesson/',
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
        )