# Generated by Django 5.0.1 on 2024-02-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_fir_crime_fir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prisoner',
            name='exit_date',
            field=models.DateField(blank=True),
        ),
    ]
