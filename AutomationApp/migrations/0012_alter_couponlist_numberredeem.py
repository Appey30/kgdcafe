# Generated by Django 4.1.3 on 2022-11-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0011_rename_is_consumed_couponlist_is_consumable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponlist',
            name='numberredeem',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
