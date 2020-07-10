from django.shortcuts import render
from django.core.mail import send_mail


def home(requests):
	return render(requests, 'index.html', {})


def about(requests):
	return render(requests, 'about.html', {})


def contact(requests):
	if requests.method == 'POST':
		message_name = requests.POST['message-name']
		message_email = requests.POST['message-email']
		message = requests.POST['message']
		messages = "\nThis message was sent by: " + message_email + "\n\n" + message

		send_mail (
			message_name, # subject
			messages, # message
			message_email, # from email
			['chaibedraa.work@gmail.com'], # to email

			)


		return render(requests, 'contact.html', {'message_name': message_name})

	else:
		return render(requests, 'contact.html', {})


def pricing(requests):
	return render(requests, 'pricing.html', {})


def service(requests):
	return  render(requests, 'service.html', {})


def appointment(requests):
	if requests.method == 'POST':
		your_name = requests.POST['your-name']
		your_phone = requests.POST['your-phone']
		your_email = requests.POST['your-email']
		your_address = requests.POST['your-address']
		your_month = requests.POST['your-month']
		your_day = requests.POST['your-day']
		your_time = requests.POST['your-time']
		your_message = requests.POST['your-message']

		appointment_message = 'Name: ' + your_name + "\nPhone: " + your_phone + "\nEmail: " + your_email + "\nAddress: " + your_address + "\nDate: " + your_day + "/" + your_month + "\nTime: " + your_time + "\nMessage: " + your_message

		send_mail (
			"Appointment request!", # subject
			appointment_message, # message
			your_email, # from email
			['chaibedraa.work@gmail.com'], # to email

			)


		return render(requests, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_month': your_month,
			'your_day': your_day,
			'your_time': your_time,
			'your_message': your_message,
			})

	else:
		return render(requests, 'index.html', {})