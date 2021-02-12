from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_email(recipient_list=None):
    subject = 'Онлайн-заказ'
    message = 'Спасибо за заказ!'
    email_from = settings.EMAIL_HOST_USER
    template = get_template('email.html')
    send_mail(subject, message, email_from, recipient_list,
              html_message=template.render())



