from django.core.management import BaseCommand
from main.models import Payment


class Command(BaseCommand):
	def handle (self, *args, **options):

		# очистка модели Category
		# records = Payment.objects.all()
		# records.delete()

		payment_list =[
			{
				'client': 'Дмитрий',
				'well_name_id': '1',
				'payment_amount': 500,
				'payment_method': 'Наличные',
			},
			{
				'client': 'Мван',
				'well_name_id': '1',
				'payment_amount': 500,
				'payment_method': 'Безнал на счет',
			},
			{
				'client': 'Сергей',
				'well_name_id': '1',
				'payment_amount': 500,
				'payment_method': 'Наличные',
			},
			{
				'client': 'Юрий',
				'well_name_id': '1',
				'payment_amount': 500,
				'payment_method': 'Безнал на счет',
			},

		]
		payment_objects =[]
		for payment_item in payment_list:
			payment_objects.append(
				Payment(**payment_item)
			)
		Payment.objects.bulk_create(payment_objects)

