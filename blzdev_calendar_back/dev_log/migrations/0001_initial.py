from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dev_logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('schedule_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='Schedules.schedules')),
            ],
        ),
    ]
