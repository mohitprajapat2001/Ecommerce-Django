# Generated by Django 4.1.7 on 2023-03-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_alter_userpayments_name_alter_userpayments_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayments',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userpayments',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpayments',
            name='product_category',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='userpayments',
            name='product_name',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='userpayments',
            name='username',
            field=models.CharField(max_length=25),
        ),
    ]
