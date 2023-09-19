from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import datetime

from users.models import User






@shared_task
def send_moderator_email():
    send_mail(
        subject='Новый комментарий',
        message='В блоге появился новый комментарий, необходимо провести ревью',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_MODERATOR]
    )


@shared_task
def check_last_login ():
    #текущее время
    today = datetime.datetime.now()

    instance = User.objects.all()
    for  i in instance:
        # Определение разницы даты последнего входа пользователя и текущей даты
        time_diff = today-i.last_login
        tdays = time_diff.days
        if tdays > 31:
            i.is_activ = False
            i.save()
            print(f'Пользователь {i.email} не активен уже {tdays} дней. Аккаунт переведен в неактивные')



# def send_moderator_likes_count():
#     likes_count = Like.objects.all().count()
#     send_mail(
#         subject='Количество лайков',
#         message=f'На {now} количество лайков: {likes_count}',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[settings.EMAIL_MODERATOR]
#     )

