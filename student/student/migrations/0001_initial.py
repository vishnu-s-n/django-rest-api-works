# Generated by Django 4.0.4 on 2023-01-04 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=120)),
                ('image', models.ImageField(null=True, upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=120)),
                ('sem', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], max_length=150)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentMarkModel_owner', to='student.studentsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('MECH', 'MECH'), ('ECE', 'ECE'), ('CIVIL', 'CIVIL')], max_length=150)),
                ('marks', models.ManyToManyField(to='student.studentmarkmodel')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.studentsmodel')),
            ],
        ),
    ]
