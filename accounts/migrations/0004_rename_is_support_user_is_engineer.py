# Generated by Django 5.0.4 on 2024-06-13 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_user_is_engineer_user_is_support_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_support",
            new_name="is_engineer",
        ),
    ]
