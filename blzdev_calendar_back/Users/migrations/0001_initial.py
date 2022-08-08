from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_primary_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30, unique=True)),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
