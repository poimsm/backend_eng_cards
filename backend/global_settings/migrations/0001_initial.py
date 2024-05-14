# Generated by Django 4.0.6 on 2024-05-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Deleted'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('extras', models.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]