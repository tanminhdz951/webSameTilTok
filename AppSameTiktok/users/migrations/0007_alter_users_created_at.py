# Generated by Django 4.1.7 on 2023-03-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_first_name_alter_users_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]