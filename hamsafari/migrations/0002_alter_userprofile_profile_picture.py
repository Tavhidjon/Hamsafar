# Generated by Django 5.1.3 on 2024-11-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamsafari', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
