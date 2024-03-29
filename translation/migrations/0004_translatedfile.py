# Generated by Django 4.2.7 on 2024-01-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_uploadedfile_delete_translatedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslatedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_file', models.FileField(upload_to='original_files/')),
                ('translated_file', models.FileField(blank=True, null=True, upload_to='translated_files/')),
                ('target_language', models.CharField(max_length=50)),
            ],
        ),
    ]
