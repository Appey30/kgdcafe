# Generated by Django 4.1.3 on 2023-01-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0019_alter_dailysales_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='messengerbag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbid', models.IntegerField(blank=True, default=0, null=True)),
                ('productname', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('categ', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('subcateg', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('size', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('chosenitemprice', models.IntegerField(blank=True, default=0, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True)),
            ],
        ),
    ]
