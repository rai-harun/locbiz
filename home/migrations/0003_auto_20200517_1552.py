# Generated by Django 3.0.6 on 2020-05-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
