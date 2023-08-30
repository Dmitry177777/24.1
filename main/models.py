from datetime import date
from users.models import User, NULLABLE
import schedule
from django.core.mail import EmailMessage
from django.db import models
from django.urls import reverse

# from django.utils.text import slugify
from pytils.translit import slugify

# NULLABLE = {'blank':True, 'null': True}

# null=False
# unique=True

class Student(models.Model):
    objects = None
    # email = models.OneToOneField(User, on_delete=models.CASCADE, default='mail',  verbose_name='почта_пользователя')
    student = models.CharField(max_length=150, verbose_name='ФИО')
    student_phone = models.CharField(max_length=350, verbose_name='Телефон', **NULLABLE)
    student_city = models.CharField(max_length=350, verbose_name='Город', **NULLABLE)
    student_avatar = models.ImageField(upload_to='student_avatar/', verbose_name='аватарка', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный клиент')

    def __str__(self):
        return f'{self.student} : {self.student_phone} : {self.student_city} '


# функция переопределяет удаление и не удаляет объект а переводит флаг is_active = False
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


    class Meta:
        verbose_name='Пользователь сервиса'
        verbose_name_plural='Пользователи сервиса'
        ordering = ('student', )

class Well(models.Model):
    objects = None
    well_name = models.CharField(max_length=150, unique=True, default='название', verbose_name='название курса')
    # email = models.OneToOneField(Student, on_delete=models.CASCADE, default='mail',  verbose_name='почта_пользователя')
    well_image = models.ImageField(upload_to='well_image/', verbose_name='превью курса', **NULLABLE)
    well_description = models.TextField(max_length=1000, verbose_name='описание курса', **NULLABLE)



    def __str__(self):
        return f' {self.well_name} : {self.well_description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



class Lesson(models.Model):
    objects = None
    # email = models.OneToOneField(Student, on_delete=models.CASCADE,  default='mail', verbose_name='почта_пользователя')
    lesson_name = models.CharField(max_length=150,  unique=True, default='', verbose_name='название урока')
    lesson_description = models.TextField(max_length=1000, verbose_name='описание урока', **NULLABLE)
    lesson_image = models.ImageField(upload_to='lesson_image/', verbose_name='превью урока', **NULLABLE)
    lesson_link = models.URLField(max_length=150, default='', verbose_name='ссылка на видео')
    well_name = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='название курса')
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    is_public = models.BooleanField (default=False)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.lesson_name}: {self.lesson_description}'



class Payment(models.Model):
    objects = None
    # email = models.OneToOneField(Student, on_delete=models.CASCADE,  default='mail', verbose_name='почта_пользователя')
    client = models.CharField(max_length=150,  unique=True, default='', verbose_name='пользователь')
    date_of_payment = models.DateTimeField(**NULLABLE)
    well_name = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    payment_amount = models.IntegerField(default=0, verbose_name='сумма оплаты')
    payment_method = models.TextField(max_length=1000, verbose_name='метод оплаты', **NULLABLE)

    class Meta:
        verbose_name = 'оплаченный курс'
        verbose_name_plural = 'оплаченные курсы'

    def __str__(self):
        return f'{self.client}: {self.well_name}'





