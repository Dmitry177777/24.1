from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Well, Lesson
from users.models import User


class MainTestCase(APITestCase):

    def setUp(self):
        Well.objects.create(id=1, well_name="5 курс")
        #создание и аутентификация суперюзера
        self.user=User.objects.create_superuser(email="admin@sky.pro", password="123456", role="MODERATOR", is_active=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создание уроков"""


        data = {
            'lesson_name': 'Matematica 31',
            'lesson_description': 'Важнейший предмет в науках',
            'lesson_link': 'https://youtube.com/',
            'well_name': 1
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
        )

        self.assertEqual(response.json(),
                         {'id': 1, 'lesson_name': 'Matematica 31', 'lesson_description': 'Важнейший предмет в науках', 'lesson_link': 'https://youtube.com/', 'well_name': 1}

                         )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""



        response = self.client.get(
            '/lesson/'
                    )

        print(response.json())

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )

    def test_create_subscription(self):
        """Тестирование создание подписки"""

        data = {
            'well_name': 1,
            'owner': 1
        }

        response = self.client.post(
            '/subscription/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
                         )

        self.assertEqual(response.json(),
                         {'id': 1, 'is_activ': False, 'well_name': 1, 'owner': 1}

                         )

    def test_list_subscription(self):
        """Тестирование вывода списка подписок"""

        response = self.client.get(
            '/subscription/'
        )

        print(response.json())

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )