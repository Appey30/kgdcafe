# Generated by Django 4.1.3 on 2023-06-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0028_buttoncolor_cardcolor_buttoncolor_textcolor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttoncolor',
            name='backgroundcolor',
            field=models.CharField(default='#f6eeea', max_length=7),
        ),
    ]