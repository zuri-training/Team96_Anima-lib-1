# Generated by Django 4.0.6 on 2022-08-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_mylib_delete_my_lib_remove_message_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lib',
            name='anima_type',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
