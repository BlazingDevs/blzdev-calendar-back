# Generated by Django 4.0.6 on 2022-08-01 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Workspaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('time', models.FloatField()),
                ('workspace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Workspaces.workspaces')),
            ],
        ),
    ]