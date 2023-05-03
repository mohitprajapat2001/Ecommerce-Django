# Generated by Django 4.1.7 on 2023-03-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_userpayments_payment_stamp_userpayments_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpayments',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userpayments',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='userpayments',
            name='email',
        ),
        migrations.AddField(
            model_name='userpayments',
            name='product_category',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpayments',
            name='product_name',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpayments',
            name='paymentstatus',
            field=models.BooleanField(default=False),
        ),
    ]