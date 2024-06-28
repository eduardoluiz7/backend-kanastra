from django.apps import AppConfig


class EmailSenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_sender'

    def ready(self):
        from django_celery_beat.models import PeriodicTask, CrontabSchedule

        schedule, created = CrontabSchedule.objects.get_or_create(
            minute='0',
            hour='8',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )

        task, created = PeriodicTask.objects.update_or_create(
            crontab=schedule,
            name='Enviar Boleto por e-mail',
            defaults={
                'crontab': schedule,
                'task':'email_sender.tasks.send_emails',
            }
        )