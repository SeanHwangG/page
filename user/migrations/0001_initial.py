# Generated by Django 3.1.7 on 2021-04-20 18:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=255)),
                ('name', models.TextField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('membership_type', models.CharField(choices=[('member', 'MEMBER'), ('admin', 'ADMIN')], default='member', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='user.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
