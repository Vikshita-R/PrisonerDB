# Generated by Django 5.0.1 on 2024-01-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_prisoner_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisoner',
            name='uuid',
            field=models.CharField(default='RAHGAN1', max_length=100),
            preserve_default=False,
        ),
    ]
