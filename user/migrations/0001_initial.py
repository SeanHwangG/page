# Generated by Django 3.1.7 on 2021-03-30 16:03

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
                ('team_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.TextField(default='', max_length=255, primary_key=True, serialize=False)),
                ('baekjoon_id', models.TextField(max_length=255, null=True)),
                ('name', models.TextField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('membership_type', models.CharField(choices=[('member', 'MEMBER'), ('admin', 'ADMIN')], default='member', max_length=255)),
                ('team', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='user.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]