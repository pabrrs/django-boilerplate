from django.db import migrations


def add_admin_user(apps, _schema):
    """
    Create `django@admin.com` user and store to database
    """
    User = apps.get_model("accounts", "User")
    User.objects.create(
        first_name="Django",
        last_name="Admin",
        email="django@admin.com",
        is_superuser=True,
        is_staff=True,
        is_active=True,
        # Decypt password: Admin@1234
        password="pbkdf2_sha256$600000$IPYVAcu7PoIqYPIR6NWhMI$yAUCsvT9qfPs1bZFpxsgpiMJ0uClBnRaANJ+3CevICM=",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_admin_user)]
