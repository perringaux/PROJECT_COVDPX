# Generated by Django 3.0.4 on 2020-03-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20200328_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='picture',
            field=models.ImageField(default=False, upload_to='picture/'),
        ),
    ]
