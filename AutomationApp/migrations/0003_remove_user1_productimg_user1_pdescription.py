# Generated by Django 4.1.3 on 2022-11-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0002_acceptorder_acknowledgedstockorder_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='Productimg',
        ),
        migrations.AddField(
            model_name='user1',
            name='PDescription',
            field=models.CharField(default='', max_length=250),
        ),
    ]
