# Generated by Django 5.0.1 on 2024-01-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisoner',
            name='uuid',
            field=models.CharField(default='1RAH', max_length=15),
            preserve_default=False,
        ),
    ]
