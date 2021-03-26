# Generated by Django 3.1.7 on 2021-03-24 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0002_auto_20210314_1258'),
        ('user', '0004_auto_20210324_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.TextField(max_length=255, primary_key=True, serialize=False)),
                ('language', models.TextField(max_length=255, null=True)),
                ('text', models.TextField(max_length=65535, null=True)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]