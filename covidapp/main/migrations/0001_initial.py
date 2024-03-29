# Generated by Django 3.2.2 on 2021-05-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid_Observations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.PositiveIntegerField(blank=True, null=True)),
                ('observationdate', models.DateField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=60, null=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('confirmed', models.IntegerField(blank=True, null=True)),
                ('deaths', models.IntegerField(blank=True, null=True)),
                ('recovered', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('filedata', models.FileField(max_length=254, upload_to='data')),
            ],
        ),
    ]
