# Generated by Django 4.1.3 on 2022-12-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0015_alter_acceptorder_customername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptorder',
            name='GSubtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='GSubtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='rejectorder',
            name='GSubtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='GSubtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7, null=True),
        ),
    ]