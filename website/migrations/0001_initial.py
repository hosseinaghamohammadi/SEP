# Generated by Django 2.1.1 on 2019-01-01 12:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CV_text', models.FileField(upload_to='')),
                ('picture', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(default='dummy', max_length=200)),
                ('companyAddress', models.CharField(default='dummy', max_length=400)),
                ('companyWebsite', models.URLField(default='google.com')),
                ('rate', models.FloatField(default=1.1)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='dummy', max_length=200)),
                ('status', models.CharField(choices=[('1', 'AVAILABLE'), ('2', 'NOT AVAILABLE')], default='AVAILABLE', max_length=20)),
                ('salary', models.IntegerField(default=1000)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('1', 'AVAILABLE'), ('2', 'NOT AVAILABLE')], default='AVAILABLE', max_length=20)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(blank=True, default='+98912988888', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='dummy', max_length=200)),
                ('jobOffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.EmpOff')),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(default='dummy', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='dummy', max_length=20)),
                ('mail', models.EmailField(default='fmansouri@gmail.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSeeker',
            fields=[
                ('name', models.CharField(default='dummy', max_length=200)),
                ('family_name', models.CharField(default='dummy', max_length=200)),
                ('studentID', models.CharField(default='95109253', max_length=8, primary_key=True, serialize=False)),
                ('nationalID', models.CharField(default='1234567891', max_length=10)),
                ('address', models.CharField(default='dummy', max_length=400)),
                ('sex', models.CharField(choices=[('1', 'MALE'), ('2', 'FEMALE')], default='FEMALE', max_length=9)),
                ('birth_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.AddField(
            model_name='systemadmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AddField(
            model_name='phone',
            name='workSeeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employee'),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='workSeeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employee'),
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AddField(
            model_name='cv',
            name='workSeeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employee'),
        ),
    ]
