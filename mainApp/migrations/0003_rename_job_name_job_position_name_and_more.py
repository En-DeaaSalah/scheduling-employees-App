# Generated by Django 4.0.1 on 2022-02-01 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_remove_employeeprofile_phone_number_employee_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_name',
            new_name='position_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='jobs',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='country',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('breakTime', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='mainApp.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='mainApp.job')),
            ],
        ),
    ]