# Generated by Django 4.1.1 on 2022-10-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='m_image1_word1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='m_image1_word2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='m_image2_word1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='m_image2_word2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='m_image3_word1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='m_image3_word2',
            field=models.CharField(default='', max_length=10),
        ),
    ]
