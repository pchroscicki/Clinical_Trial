# Generated by Django 4.0.3 on 2022-04-10 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CT_platform', '0003_alter_patients_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='visit_author',
            new_name='author',
        ),
    ]
