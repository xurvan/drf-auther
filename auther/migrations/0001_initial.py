# Generated by Django 3.2.5 on 2021-07-18 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(unique=True)),
                ('address', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(null=True, unique=True)),
                ('regex', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(unique=True)),
                ('level', models.IntegerField(default=0)),
                ('perms', models.ManyToManyField(related_name='roles', to='auther.Perm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.TextField(null=True)),
                ('username', models.TextField(max_length=64, null=True, unique=True)),
                ('email', models.EmailField(max_length=320, null=True, unique=True)),
                ('phone', models.BigIntegerField(null=True, unique=True)),
                ('password', models.TextField(max_length=64)),
                ('active', models.BooleanField(default=True)),
                ('expire', models.DateTimeField(null=True)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='users', to='auther.domain')),
                ('roles', models.ManyToManyField(related_name='users', to='auther.Role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('token', models.TextField(max_length=64, unique=True)),
                ('user_agent', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sessions', to='auther.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
