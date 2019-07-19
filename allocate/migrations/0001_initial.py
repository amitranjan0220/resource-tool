# Generated by Django 2.2 on 2019-07-18 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchByUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SearchByResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_resource.Category')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_resource.MyResource')),
            ],
        ),
        migrations.CreateModel(
            name='AllocateResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=None, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_resource.MyResource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
