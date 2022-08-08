from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('Workspaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('time', models.FloatField()),
                ('workspace_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='Workspaces.workspaces')),
                ('users', models.ManyToManyField(blank=True, to='Users.user')),
            ],
        ),
    ]
