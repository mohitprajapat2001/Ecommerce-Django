# Generated by Django 4.1.3 on 2023-02-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('dob', models.DateTimeField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('profession', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]