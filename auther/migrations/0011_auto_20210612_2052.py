# Generated by Django 3.2.3 on 2021-06-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0010_auto_20210609_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='perm',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
