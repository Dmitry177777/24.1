# Generated by Django 4.2.3 on 2023-08-26 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=150, verbose_name='ФИО')),
                ('student_phone', models.CharField(blank=True, max_length=350, null=True, verbose_name='Телефон')),
                ('student_city', models.CharField(blank=True, max_length=350, null=True, verbose_name='Город')),
                ('student_avatar', models.ImageField(blank=True, null=True, upload_to='student_avatar/', verbose_name='аватарка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный клиент')),
            ],
            options={
                'verbose_name': 'Пользователь сервиса',
                'verbose_name_plural': 'Пользователи сервиса',
                'ordering': ('student',),
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_name', models.CharField(default='название', max_length=150, unique=True, verbose_name='название курса')),
                ('well_image', models.ImageField(blank=True, null=True, upload_to='well_image/', verbose_name='превью курса')),
                ('well_description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='описание курса')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(default='', max_length=150, unique=True, verbose_name='название урока')),
                ('lesson_description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='описание урока')),
                ('lesson_image', models.ImageField(blank=True, null=True, upload_to='lesson_image/', verbose_name='превью урока')),
                ('lesson_link', models.URLField(default='', max_length=150, unique=True, verbose_name='ссылка на видео')),
                ('well_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.well', verbose_name='название курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
