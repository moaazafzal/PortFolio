# Generated by Django 2.2.6 on 2019-11-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]