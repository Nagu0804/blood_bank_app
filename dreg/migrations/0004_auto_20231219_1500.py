# Generated by Django 2.2.8 on 2023-12-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0003_auto_20231219_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorlist',
            name='last_donate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
