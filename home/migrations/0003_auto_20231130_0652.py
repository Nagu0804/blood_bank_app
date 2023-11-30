# Generated by Django 3.1.4 on 2023-11-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231129_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagebody',
            name='body_img',
            field=models.ImageField(blank=True, null=True, upload_to='home_body'),
        ),
        migrations.AlterField(
            model_name='homepageslider',
            name='id_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepageslider',
            name='slider_1',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AlterField(
            model_name='homepageslider',
            name='slider_2',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AlterField(
            model_name='homepageslider',
            name='slider_3',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AlterField(
            model_name='homepageslider',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
