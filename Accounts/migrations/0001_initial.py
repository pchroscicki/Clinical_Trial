# Generated by Django 4.0.3 on 2022-04-10 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.SmallIntegerField(choices=[(1, 'Clinical Research Associate'), (2, 'Medical Doctor'), (3, 'Pharmacologist'), (4, 'EMA officer')])),
                ('site_name', models.CharField(max_length=255)),
                ('site_adress', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
