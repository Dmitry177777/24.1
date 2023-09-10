"""создание платежа"""
import requests

from config import settings


def payment_intents_create(instance):

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    amount = instance.payment_amount
    well = instance.well_name


    data = f'unit_amount={amount}&currency = eur & recurring[interval] = month & product = {well}'
    encoded_data = data.encode('utf-8')


    response = requests.post(
        f'{settings.STRIPE_CREATE_URL}',
        headers=headers,
        data=encoded_data,
        auth=(f'{settings.STRIPE_AUTH}', ''),
    )

    print(response)
    return response

"""получение платежа"""
def payment_intents_retrieve(instance):
    response = requests.get(
        f'{settings.STRIPE_RETRIEVE_URL}',
        auth=(f'{settings.STRIPE_AUTH}', ''),
    )

    return response





