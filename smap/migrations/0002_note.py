# Generated by Django 3.2.12 on 2023-03-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('clas', models.CharField(max_length=5)),
                ('image', models.ImageField(upload_to='smap/images')),
            ],
        ),
    ]
