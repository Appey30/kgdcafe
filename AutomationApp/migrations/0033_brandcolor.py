# Generated by Django 4.1.3 on 2023-07-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutomationApp', '0032_buttoncolor_body_bold_buttoncolor_body_italic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brandcolor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(blank=True, default='2', null=True)),
                ('text', models.CharField(blank=True, default='#2c170c', max_length=7, null=True)),
                ('button', models.CharField(blank=True, default='#aa5c31', max_length=7, null=True)),
                ('container', models.CharField(blank=True, default='#d4ad98', max_length=7, null=True)),
                ('background', models.CharField(blank=True, default='#f6eeea', max_length=7, null=True)),
                ('identifier', models.CharField(blank=True, default='#2c170c#aa5c31#d4ad98#f6eeea', max_length=50, null=True)),
            ],
        ),
    ]