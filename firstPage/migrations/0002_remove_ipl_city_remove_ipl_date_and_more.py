# Generated by Django 5.0.1 on 2024-01-23 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipl',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='dl_applied',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='player_of_match',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='result',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='toss_decision',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='toss_winner',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='umpire1',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='umpire2',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='umpire3',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='win_by_runs',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='win_by_wickets',
        ),
        migrations.RemoveField(
            model_name='ipl',
            name='winner',
        ),
        migrations.AlterField(
            model_name='ipl',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
