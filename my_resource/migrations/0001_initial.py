# Generated by Django 2.2 on 2019-07-18 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsc_name', models.CharField(max_length=100)),
                ('rsc_ip', models.CharField(max_length=20)),
                ('rsc_comment', models.TextField(max_length=50)),
                ('rsc_status', models.CharField(choices=[('Unassigned', 'Unassigned'), ('Assigned', 'Assigned')], default='Unassigned', max_length=30)),
                ('rsc_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_resource.Category')),
            ],
        ),
    ]
