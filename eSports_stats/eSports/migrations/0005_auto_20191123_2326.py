# Generated by Django 2.2.6 on 2019-11-23 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSports', '0004_auto_20191123_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
