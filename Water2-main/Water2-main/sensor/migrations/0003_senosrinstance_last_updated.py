# Generated by Django 4.2.7 on 2023-11-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_senosrinstance_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='senosrinstance',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]