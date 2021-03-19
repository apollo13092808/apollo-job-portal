# Generated by Django 3.1.6 on 2021-02-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], max_length=20, null=True),
        ),
    ]