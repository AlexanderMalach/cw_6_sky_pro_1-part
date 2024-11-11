from django.conf import settings
from django.core.mail import send_mail

from newsletters.models import Mailing


# from django.models import Mailing
# from django.models  import Client


def send_order_email(mailing_item: Mailing):
    send_mail(
        'Заявка на покупку лодки',
        f'{mailing_item.name} ({mailing_item.email}) хочет купить вашу лодку{mailing_item.client.name}. '
        f'Вот сообщение {mailing_item.message}',
        settings.EMAIL_HOST_USER,
        [mailing_item.client.owner.email]
    )


