# Generated by Django 4.1.3 on 2023-01-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0020_messengerbag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messengerbag',
            name='fbid',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]