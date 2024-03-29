# Generated by Django 4.0.6 on 2023-08-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_question_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Deleted'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('questions_type', models.TextField(default='random')),
                ('questions_search', models.TextField(default='random')),
                ('ids', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question_config',
            },
        ),
    ]
