# Generated by Django 3.2.6 on 2022-04-27 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_hub', '0013_speciality_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='url',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_doctors', to='hospital_hub.hospital'),
        ),
    ]