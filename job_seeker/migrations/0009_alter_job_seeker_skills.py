# Generated by Django 4.2.7 on 2024-02-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0008_remove_job_seeker_bio_remove_job_seeker_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]