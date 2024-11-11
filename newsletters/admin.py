from django.contrib import admin

from newsletters.models import Client, Message, Mailing, MailingAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "email", "phone_number")
    search_fields = (
        "fullname",
        "email",
        "phone_number",
    )
    list_filter = (
        "fullname",
        "email",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "subject_message")
    search_fields = ("subject_message",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_created",
        "message",
        "frequency",
        "status",
    )


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "attempt_datetime",
        "status",
        "server_response",
    )
    list_filter = ("attempt_datetime",)
