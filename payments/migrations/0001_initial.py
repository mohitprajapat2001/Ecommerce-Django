# Generated by Django 4.1.7 on 2023-03-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userpayments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('payment_stamp', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('paymentstatus', models.BooleanField()),
            ],
        ),
    ]