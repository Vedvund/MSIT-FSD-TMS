# Generated by Django 4.0.4 on 2022-04-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_alter_useranswerfileupload_answer_text_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswerfileupload',
            name='answer_text_input',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
