# Generated by Django 4.1.7 on 2023-03-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_alter_userpayments_name_alter_userpayments_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayments',
            name='available',
            field=models.IntegerField(default=1),
        ),
    ]