# Generated by Django 3.1.3 on 2021-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booksale'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksale',
            name='year',
            field=models.IntegerField(default=1976),
            preserve_default=False,
        ),
    ]