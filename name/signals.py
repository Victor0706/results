from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Response


@receiver(post_save, sender=Response)
def response_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        article__author=instance.author
    ).values_list('email', flat=True)

    subject = f'Новый отклик на статью {instance.author}'

    text_content = (
        f'Статья: {instance.article}\n'
        f'Текст: {instance.text}\n\n'
        f'Ссылка на товар: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Статья: {instance.article}<br>'
        f'Текст: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


