# Generated by Django 4.1.3 on 2023-02-25 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0025_remove_fingerprint_employee_delete_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='Productimg',
        ),
    ]
