# Generated by Django 4.2.7 on 2023-11-11 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ticket_assignee_ticket_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]