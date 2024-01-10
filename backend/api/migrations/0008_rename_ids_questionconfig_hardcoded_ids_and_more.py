# Generated by Django 4.0.6 on 2023-08-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_questionconfig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionconfig',
            old_name='ids',
            new_name='hardcoded_ids',
        ),
        migrations.AddField(
            model_name='questionconfig',
            name='starting_questions',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
