# Generated by Django 4.0.3 on 2022-04-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_alter_makequestion_max_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makequestion',
            name='difficulty_level',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
