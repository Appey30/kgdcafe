# Generated by Django 4.1.3 on 2022-11-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0009_remove_couponlist_is_withvalidity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couponlist',
            name='qr',
        ),
    ]