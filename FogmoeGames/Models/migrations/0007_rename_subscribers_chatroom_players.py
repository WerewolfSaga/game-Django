# Generated by Django 5.0.1 on 2024-01-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0006_werewolfsaga_action_werewolfsaga_round'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroom',
            old_name='subscribers',
            new_name='players',
        ),
    ]
