# Generated by Django 2.1.1 on 2019-01-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20181231_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='dummy', max_length=20, primary_key=True, serialize=False),
        ),
    ]
