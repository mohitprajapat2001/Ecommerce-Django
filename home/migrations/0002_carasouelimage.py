# Generated by Django 4.1.7 on 2023-04-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carasouelimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='carasouel_image')),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]
