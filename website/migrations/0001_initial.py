# Generated by Django 2.1.1 on 2018-12-31 11:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('companyAddress', models.CharField(max_length=400)),
                ('companyWebsite', models.URLField()),
                ('rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='WorkSeeker',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('family_name', models.CharField(max_length=200)),
                ('studentID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nationalID', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=400)),
                ('sex', models.BooleanField(default=0)),
                ('birth_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='workSeeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.WorkSeeker'),
        ),
    ]
