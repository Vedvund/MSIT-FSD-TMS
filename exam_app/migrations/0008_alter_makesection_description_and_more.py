# Generated by Django 4.0.3 on 2022-04-22 03:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0007_alter_makesection_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makesection',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='makesection',
            name='instructions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
