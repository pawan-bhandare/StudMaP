# Generated by Django 3.2.12 on 2023-03-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smap', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='sub',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='clas',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='note',
            name='dept',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
