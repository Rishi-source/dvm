# Generated by Django 4.2 on 2023-05-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0012_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
