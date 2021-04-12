# Generated by Django 3.1.4 on 2021-01-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='perm',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]
