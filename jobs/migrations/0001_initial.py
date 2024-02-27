# Generated by Django 4.2.7 on 2024-01-14 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('job_seeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('requirements', models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('RESTful APIs', 'RESTful APIs'), ('Database', 'Database'), ('Version Control', 'Version Control'), ('Frontend Frameworks', 'Frontend Frameworks'), ('Testing', 'Testing'), ('Web Security', 'Web Security'), ('Responsive Design', 'Responsive Design'), ('Git', 'Git'), ('Debugging', 'Debugging'), ('Agile/Scrum', 'Agile/Scrum'), ('Problem Solving', 'Problem Solving'), ('Communication', 'Communication'), ('Collaboration', 'Collaboration'), ('Continuous Integration', 'Continuous Integration'), ('Documentation', 'Documentation')], max_length=70)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, upload_to='application/')),
                ('letter', models.TextField()),
                ('applied', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seeker.job_seeker')),
            ],
        ),
    ]
