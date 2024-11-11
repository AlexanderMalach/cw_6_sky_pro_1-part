from django.db import models


# Create your models here.
class Client(models.Model):
    """Сервис для клиента"""

    email = models.CharField(max_length=250, verbose_name="Email", unique=True)
    phone_number = models.CharField(
        max_length=15, verbose_name="Phone number", unique=True, blank=True, null=True
    )
    fullname = models.CharField(max_length=250, verbose_name="Full name")
    comment = models.TextField(verbose_name="Comment")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.fullname


class Message(models.Model):
    """Сообщение"""

    subject_message = models.TextField(verbose_name="text_subject")
    body_message = models.TextField(verbose_name="text_message")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.subject_message


class Mailing(models.Model):
    """Рассылка"""

    class Frequency(models.TextChoices):
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"
        MONTHLY = "monthly", "Monthly"

    class Status(models.TextChoices):
        CREATED = "created", "Created"
        STARTED = "started", "Started"
        FINISHED = "finished", "Finished"

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    frequency = models.CharField(max_length=10, choices=Frequency.choices)
    status = models.CharField(
            max_length=10, choices=Status.choices, default=Status.CREATED
    )
    message = models.ForeignKey("Message", on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, related_name="clients")

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
        ordering = ["-date_created"]

    def __str__(self):
        return f"Mailing on {self.date_created} - {self.status}"


class MailingAttempt(models.Model):
    """Попытка рассылки"""

    class StatusSuccess(models.TextChoices):
        SUCCESS = "success", "Успешно"
        FAILED = "failed", "Неуспешно"

    attempt_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=StatusSuccess.choices)
    server_response = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Mailing attempt"
        verbose_name_plural = "Mailing attempts"
        ordering = ["-attempt_datetime"]

    def __str__(self):
        return f"Attempt on {self.attempt_datetime} - {self.status}"
