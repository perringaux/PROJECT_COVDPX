# Generated by Django 3.0.4 on 2020-03-28 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20200328_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='posts',
        ),
        migrations.AddField(
            model_name='like',
            name='author',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='db.Profil'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='db.Profil'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='author',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='db.Profil'),
        ),
    ]
