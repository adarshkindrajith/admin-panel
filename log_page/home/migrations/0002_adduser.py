# Generated by Django 5.1.3 on 2024-12-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
