# Generated by Django 4.1.7 on 2023-04-27 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_carasouelimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carasouelimage',
            name='name',
        ),
    ]