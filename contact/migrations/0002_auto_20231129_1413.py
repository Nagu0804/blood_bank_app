# Generated by Django 3.1.4 on 2023-11-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpagebody',
            name='contact_text',
            field=models.TextField(blank=True, default='Enter the address', null=True),
        ),
    ]
