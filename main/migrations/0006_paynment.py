# Generated by Django 4.2.3 on 2023-08-29 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_lesson_lesson_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paynment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(default='', max_length=150, unique=True, verbose_name='пользователь')),
                ('date_of_payment', models.DateTimeField()),
                ('payment_amount', models.IntegerField(default=0, verbose_name='сумма оплаты')),
                ('payment_method', models.TextField(blank=True, max_length=1000, null=True, verbose_name='метод оплаты')),
                ('well_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.well', verbose_name='оплаченный курс')),
            ],
            options={
                'verbose_name': 'оплаченный курс',
                'verbose_name_plural': 'оплаченные курсы',
            },
        ),
    ]
