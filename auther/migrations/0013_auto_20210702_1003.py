# Generated by Django 3.2.3 on 2021-07-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0012_auto_20210621_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar_token',
        ),
        migrations.AlterField(
            model_name='domain',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='perm',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]