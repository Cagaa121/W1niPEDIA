# Generated by Django 5.0.1 on 2024-01-25 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='create_at',
            new_name='created_at',
        ),
    ]