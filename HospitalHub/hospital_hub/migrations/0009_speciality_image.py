# Generated by Django 3.2.6 on 2022-04-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_hub', '0008_hospital_specialities'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
