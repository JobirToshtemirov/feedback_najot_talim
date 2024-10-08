# Generated by Django 5.1.1 on 2024-10-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
    ]
