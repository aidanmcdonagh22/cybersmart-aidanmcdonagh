# Generated by Django 3.2.9 on 2021-11-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('content', models.CharField(blank=True, max_length=250)),
                ('done', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=75, null=True)),
                ('temp', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
