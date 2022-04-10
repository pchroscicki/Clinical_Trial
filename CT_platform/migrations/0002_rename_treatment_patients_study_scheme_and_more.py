# Generated by Django 4.0.3 on 2022-04-10 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CT_platform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='treatment',
            new_name='study_scheme',
        ),
        migrations.AlterField(
            model_name='patients',
            name='drug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CT_platform.drug'),
        ),
    ]
