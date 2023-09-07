"""создание платежа"""
import requests

from config import settings


def payment_intents_create(instance):

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    amount = instance.payment_amount


    data = f'amount={amount}&currency=usd&automatic_payment_methods[enabled]=true'

    response = requests.post(
        f'{settings.STRIPE_CREATE_URL}',
        headers=headers,
        data=data,
        auth=(f'{settings.STRIPE_AUTH}', ''),
    )
    return response

"""получение платежа"""
def payment_intents_retrieve(instance):
    response = requests.get(
        f'{settings.STRIPE_RETRIEVE_URL}',
        auth=(f'{settings.STRIPE_AUTH}', ''),
    )

    return response





