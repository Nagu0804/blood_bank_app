# Generated by Django 2.2.8 on 2023-12-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vision', models.IntegerField(blank=True, null=True)),
                ('title1', models.CharField(blank=True, max_length=20, null=True)),
                ('title2', models.CharField(blank=True, max_length=20, null=True)),
                ('title3', models.CharField(blank=True, max_length=20, null=True)),
                ('body_img1', models.ImageField(blank=True, null=True, upload_to='home_body')),
                ('body_img2', models.ImageField(blank=True, null=True, upload_to='home_body')),
                ('body_img3', models.ImageField(blank=True, null=True, upload_to='home_body')),
                ('body_text1', models.TextField(blank=True, null=True)),
                ('body_text2', models.TextField(blank=True, null=True)),
                ('body_text3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('slider_1', models.ImageField(blank=True, null=True, upload_to='slider')),
                ('slider_2', models.ImageField(blank=True, null=True, upload_to='slider')),
                ('slider_3', models.ImageField(blank=True, null=True, upload_to='slider')),
            ],
        ),
    ]
