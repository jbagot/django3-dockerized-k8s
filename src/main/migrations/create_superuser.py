from django.db import models, migrations

from django.contrib.auth import get_user_model
from django.conf import settings


def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create_superuser(
        settings.SUPERUSER_NAME, settings.SUPERUSER_EMAIL, settings.SUPERUSER_PASSWORD
    )


def delete_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.filter(email=settings.SUPERUSER_EMAIL).delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(
            create_superuser,
            reverse_code=delete_superuser
        ),
    ]
